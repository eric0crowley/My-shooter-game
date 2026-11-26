export const MATCH_TEAMS = Object.freeze(['blue', 'red']);

const DEFAULT_DURATION_SECONDS = 180;
const DEFAULT_SCORE_LIMIT = 20;

function positiveNumber(value, fallback) {
  const number = Number(value);
  return Number.isFinite(number) && number > 0 ? number : fallback;
}

export class MatchSession {
  constructor({ durationSeconds = DEFAULT_DURATION_SECONDS, scoreLimit = DEFAULT_SCORE_LIMIT } = {}) {
    this.durationSeconds = positiveNumber(durationSeconds, DEFAULT_DURATION_SECONDS);
    this.scoreLimit = Math.max(1, Math.floor(positiveNumber(scoreLimit, DEFAULT_SCORE_LIMIT)));
    this.reset();
  }

  reset() {
    this.phase = 'ready';
    this.remainingSeconds = this.durationSeconds;
    this.scores = Object.fromEntries(MATCH_TEAMS.map((team) => [team, 0]));
    this.winner = null;
    this.endReason = null;
  }

  start() {
    this.reset();
    this.phase = 'active';
    return this.snapshot();
  }

  recordKill(team) {
    if (this.phase !== 'active' || !Object.hasOwn(this.scores, team)) return false;
    this.scores[team]++;
    if (this.scores[team] >= this.scoreLimit) this.finish(team, 'score-limit');
    return true;
  }

  update(deltaSeconds) {
    if (this.phase !== 'active') return false;
    const delta = Number(deltaSeconds);
    if (!Number.isFinite(delta) || delta <= 0) return false;

    this.remainingSeconds = Math.max(0, this.remainingSeconds - delta);
    if (this.remainingSeconds === 0) {
      const [blue, red] = MATCH_TEAMS.map((team) => this.scores[team]);
      const winner = blue === red ? 'draw' : blue > red ? 'blue' : 'red';
      this.finish(winner, 'time-limit');
    }
    return this.phase === 'finished';
  }

  finish(winner, reason) {
    if (this.phase !== 'active') return false;
    this.phase = 'finished';
    this.winner = winner;
    this.endReason = reason;
    return true;
  }

  snapshot() {
    return {
      phase: this.phase,
      remainingSeconds: this.remainingSeconds,
      durationSeconds: this.durationSeconds,
      scoreLimit: this.scoreLimit,
      scores: { ...this.scores },
      winner: this.winner,
      endReason: this.endReason,
    };
  }
}
