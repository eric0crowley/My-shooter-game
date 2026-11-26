import test from 'node:test';
import assert from 'node:assert/strict';
import { MatchSession } from '../src/MatchSession.js';

test('match starts with clean team scores and a fixed clock', () => {
  const match = new MatchSession({ durationSeconds: 90, scoreLimit: 3 });
  assert.equal(match.snapshot().phase, 'ready');

  const started = match.start();
  assert.equal(started.phase, 'active');
  assert.equal(started.remainingSeconds, 90);
  assert.deepEqual(started.scores, { blue: 0, red: 0 });
});

test('first team to the score limit wins and further scoring is rejected', () => {
  const match = new MatchSession({ durationSeconds: 60, scoreLimit: 2 });
  match.start();

  assert.equal(match.recordKill('blue'), true);
  assert.equal(match.recordKill('unknown'), false);
  assert.equal(match.recordKill('red'), true);
  assert.equal(match.recordKill('blue'), true);
  assert.equal(match.phase, 'finished');
  assert.equal(match.winner, 'blue');
  assert.equal(match.endReason, 'score-limit');
  assert.equal(match.recordKill('red'), false);
});

test('time limit chooses the leading team and reports a draw when scores tie', () => {
  const match = new MatchSession({ durationSeconds: 10, scoreLimit: 20 });
  match.start();
  match.recordKill('red');
  assert.equal(match.update(4), false);
  assert.equal(match.snapshot().remainingSeconds, 6);
  assert.equal(match.update(9), true);
  assert.equal(match.winner, 'red');
  assert.equal(match.endReason, 'time-limit');

  match.start();
  match.recordKill('blue');
  match.recordKill('red');
  match.update(10);
  assert.equal(match.winner, 'draw');
});

test('invalid elapsed time cannot change a live match clock', () => {
  const match = new MatchSession();
  match.start();
  for (const delta of [0, -1, Number.NaN, Number.POSITIVE_INFINITY]) match.update(delta);
  assert.equal(match.phase, 'active');
  assert.equal(match.remainingSeconds, 180);
});
