import test from 'node:test';
import assert from 'node:assert/strict';
import {
  DEFAULT_PLAYER_PROFILE,
  PLAYER_PROFILE_KEY,
  getProfileProgress,
  loadPlayerProfile,
  recordMatchResult,
  savePlayerProfile,
  sanitizePlayerName,
  sanitizePlayerProfile,
  setPreferredWeapon,
  setProfileName,
  xpRequiredForLevel,
} from '../src/PlayerProfile.js';

function createMemoryStorage(initial = {}) {
  const values = new Map(Object.entries(initial));
  return {
    getItem(key) { return values.has(key) ? values.get(key) : null; },
    setItem(key, value) { values.set(key, String(value)); },
    removeItem(key) { values.delete(key); },
  };
}

test('local profile has a safe first-run identity and level-one progress', () => {
  const profile = loadPlayerProfile(createMemoryStorage());
  assert.equal(profile.name, 'بازیکن');
  assert.equal(profile.preferredWeapon, 'rifle');
  assert.equal(getProfileProgress(profile).level, 1);
  assert.equal(getProfileProgress(profile).rank, 'سرباز');
});

test('profile names cap Unicode characters without splitting a surrogate pair', () => {
  assert.equal(sanitizePlayerName('🪖'.repeat(22)), '🪖'.repeat(20));
});

test('profile data is clamped, normalized and rejects an unknown weapon id', () => {
  const profile = sanitizePlayerProfile({
    name: '  <بازیکن>\n\u0000',
    preferredWeapon: 'not-a-real-gun',
    totalXp: -50,
    stats: { matches: 2.8, wins: -4, kills: '6', bestWave: 99_999 },
  });
  assert.equal(profile.name, '<بازیکن>');
  assert.equal(profile.preferredWeapon, 'rifle');
  assert.equal(profile.totalXp, 0);
  assert.equal(profile.stats.matches, 2);
  assert.equal(profile.stats.wins, 0);
  assert.equal(profile.stats.kills, 6);
  assert.equal(profile.stats.bestWave, 10_000);
});

test('local profile name and preferred weapon can be changed without touching match stats', () => {
  const base = sanitizePlayerProfile(DEFAULT_PLAYER_PROFILE);
  const named = setProfileName(base, '  تکاور من  ');
  const equipped = setPreferredWeapon(named, 'shotgun');
  const fallback = setPreferredWeapon(equipped, 'missing');
  assert.equal(equipped.name, 'تکاور من');
  assert.equal(equipped.preferredWeapon, 'shotgun');
  assert.equal(fallback.preferredWeapon, 'rifle');
  assert.equal(equipped.stats.matches, 0);
});

test('profile survives reload through storage and malformed records fall back safely', () => {
  const storage = createMemoryStorage();
  const profile = setProfileName(DEFAULT_PLAYER_PROFILE, 'Viper');
  savePlayerProfile(profile, storage);
  assert.equal(PLAYER_PROFILE_KEY, 'rage-of-fight.profile.v1');
  assert.deepEqual(loadPlayerProfile(storage), profile);

  storage.setItem(PLAYER_PROFILE_KEY, '{broken');
  assert.equal(loadPlayerProfile(storage).name, DEFAULT_PLAYER_PROFILE.name);
});

test('TDM result awards local XP and updates match outcome and lifetime K/D totals', () => {
  const outcome = recordMatchResult(DEFAULT_PLAYER_PROFILE, {
    mode: 'tdm',
    kills: 4,
    deaths: 2,
    winner: 'blue',
  });
  assert.equal(outcome.earnedXp, 100);
  assert.equal(outcome.profile.stats.matches, 1);
  assert.equal(outcome.profile.stats.wins, 1);
  assert.equal(outcome.profile.stats.kills, 4);
  assert.equal(outcome.profile.stats.deaths, 2);
  assert.equal(outcome.level, 1);
});

test('level thresholds carry XP forward and report level-ups', () => {
  const profile = { ...DEFAULT_PLAYER_PROFILE, totalXp: xpRequiredForLevel(1) - 30 };
  const outcome = recordMatchResult(profile, { mode: 'tdm', kills: 2, winner: 'blue' });
  assert.equal(outcome.previousLevel, 1);
  assert.equal(outcome.level, 2);
  assert.equal(outcome.levelsGained, 1);
  assert.equal(getProfileProgress(outcome.profile).xpIntoLevel, 50);
});

test('zombie runs track best wave while practice does not award competitive wins', () => {
  const first = recordMatchResult(DEFAULT_PLAYER_PROFILE, {
    mode: 'zombie',
    kills: 7,
    deaths: 1,
    wave: 3,
  });
  const second = recordMatchResult(first.profile, {
    mode: 'training',
    kills: 2,
    wave: 1,
  });
  assert.equal(first.earnedXp, 92);
  assert.equal(first.profile.stats.bestWave, 3);
  assert.equal(second.profile.stats.matches, 2);
  assert.equal(second.profile.stats.wins, 0);
  assert.equal(second.profile.stats.bestWave, 3);
});

test('profile storage denial leaves an immediately usable in-memory profile', () => {
  const denied = {
    getItem() { throw new Error('blocked'); },
    setItem() { throw new Error('blocked'); },
  };
  const profile = savePlayerProfile(setProfileName(DEFAULT_PLAYER_PROFILE, 'Offline'), denied);
  assert.equal(profile.name, 'Offline');
  assert.equal(loadPlayerProfile(denied).name, DEFAULT_PLAYER_PROFILE.name);
});
