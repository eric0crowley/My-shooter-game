export const PLAYER_PROFILE_KEY = 'rage-of-fight.profile.v1';
export const MAX_PROFILE_LEVEL = 50;
export const PLAYER_WEAPON_IDS = Object.freeze(['rifle', 'pistol', 'shotgun']);

const DEFAULT_STATS = Object.freeze({
  matches: 0,
  wins: 0,
  losses: 0,
  draws: 0,
  kills: 0,
  deaths: 0,
  bestWave: 0,
});

export const DEFAULT_PLAYER_PROFILE = Object.freeze({
  name: 'بازیکن',
  preferredWeapon: 'rifle',
  totalXp: 0,
  stats: DEFAULT_STATS,
});

const RANKS = Object.freeze([
  { level: 1, title: 'سرباز' },
  { level: 5, title: 'تکاور' },
  { level: 10, title: 'رزم‌آزموده' },
  { level: 20, title: 'نخبه' },
  { level: 35, title: 'فرمانده' },
]);

function storageOrNull(storage) {
  if (storage !== undefined) return storage;
  try {
    return globalThis.localStorage || null;
  } catch {
    return null;
  }
}

function wholeNumber(value, maximum = 1_000_000_000) {
  const number = Number(value);
  if (!Number.isFinite(number)) return 0;
  return Math.max(0, Math.min(maximum, Math.floor(number)));
}

export function sanitizePlayerName(value) {
  const name = [...String(value ?? '').replace(/[\u0000-\u001f\u007f]/g, '').trim()]
    .slice(0, 20)
    .join('');
  return name || DEFAULT_PLAYER_PROFILE.name;
}

export function xpRequiredForLevel(level) {
  const safeLevel = Math.max(1, Math.min(MAX_PROFILE_LEVEL, Math.floor(Number(level) || 1)));
  return 120 + (safeLevel - 1) * 45;
}

function xpRequiredToReachLevel(level) {
  let total = 0;
  for (let current = 1; current < level; current++) {
    total += xpRequiredForLevel(current);
  }
  return total;
}

export function getProfileProgress(profile) {
  const totalXp = wholeNumber(profile?.totalXp);
  let level = 1;
  let xpRemaining = totalXp;

  while (level < MAX_PROFILE_LEVEL) {
    const requirement = xpRequiredForLevel(level);
    if (xpRemaining < requirement) break;
    xpRemaining -= requirement;
    level++;
  }

  const rank = [...RANKS].reverse().find((entry) => level >= entry.level) || RANKS[0];
  const xpForNextLevel = level === MAX_PROFILE_LEVEL ? 0 : xpRequiredForLevel(level);
  return {
    level,
    rank: rank.title,
    totalXp,
    xpIntoLevel: level === MAX_PROFILE_LEVEL ? xpRemaining : Math.min(xpRemaining, xpForNextLevel),
    xpForNextLevel,
    progress: xpForNextLevel === 0 ? 1 : Math.min(1, xpRemaining / xpForNextLevel),
    nextLevelXp: level === MAX_PROFILE_LEVEL
      ? totalXp
      : xpRequiredToReachLevel(level + 1),
  };
}

export function sanitizePlayerProfile(profile = {}) {
  const source = profile && typeof profile === 'object' ? profile : {};
  const sourceStats = source.stats && typeof source.stats === 'object' ? source.stats : {};
  const preferredWeapon = PLAYER_WEAPON_IDS.includes(source.preferredWeapon)
    ? source.preferredWeapon
    : DEFAULT_PLAYER_PROFILE.preferredWeapon;

  return {
    name: sanitizePlayerName(source.name),
    preferredWeapon,
    totalXp: wholeNumber(source.totalXp),
    stats: {
      matches: wholeNumber(sourceStats.matches),
      wins: wholeNumber(sourceStats.wins),
      losses: wholeNumber(sourceStats.losses),
      draws: wholeNumber(sourceStats.draws),
      kills: wholeNumber(sourceStats.kills),
      deaths: wholeNumber(sourceStats.deaths),
      bestWave: wholeNumber(sourceStats.bestWave, 10_000),
    },
  };
}

export function loadPlayerProfile(storage) {
  try {
    const raw = storageOrNull(storage)?.getItem(PLAYER_PROFILE_KEY);
    return raw
      ? sanitizePlayerProfile(JSON.parse(raw))
      : sanitizePlayerProfile(DEFAULT_PLAYER_PROFILE);
  } catch {
    return sanitizePlayerProfile(DEFAULT_PLAYER_PROFILE);
  }
}

export function savePlayerProfile(profile, storage) {
  const normalized = sanitizePlayerProfile(profile);
  try {
    storageOrNull(storage)?.setItem(PLAYER_PROFILE_KEY, JSON.stringify(normalized));
  } catch {
    // Storage can be disabled in private browsing or some Android WebViews.
  }
  return normalized;
}

export function setProfileName(profile, name) {
  return sanitizePlayerProfile({ ...profile, name: sanitizePlayerName(name) });
}

export function setPreferredWeapon(profile, weaponId) {
  const preferredWeapon = PLAYER_WEAPON_IDS.includes(weaponId)
    ? weaponId
    : DEFAULT_PLAYER_PROFILE.preferredWeapon;
  return sanitizePlayerProfile({ ...profile, preferredWeapon });
}

export function recordMatchResult(profile, result = {}) {
  const normalized = sanitizePlayerProfile(profile);
  const mode = ['training', 'zombie', 'tdm'].includes(result.mode)
    ? result.mode
    : 'training';
  const kills = wholeNumber(result.kills, 10_000);
  const deaths = wholeNumber(result.deaths, 10_000);
  const wave = wholeNumber(result.wave, 10_000);
  const winner = ['blue', 'red', 'draw'].includes(result.winner)
    ? result.winner
    : null;

  let earnedXp = 5;
  if (mode === 'tdm') {
    earnedXp = 25 + kills * 10 + (winner === 'blue' ? 35 : winner === 'draw' ? 20 : 10);
  } else if (mode === 'zombie') {
    earnedXp = 10 + kills * 4 + wave * 18;
  } else {
    earnedXp = 5 + kills * 3;
  }
  earnedXp = Math.min(600, wholeNumber(earnedXp, 600));

  const nextProfile = sanitizePlayerProfile({
    ...normalized,
    totalXp: Math.min(1_000_000_000, normalized.totalXp + earnedXp),
    stats: {
      ...normalized.stats,
      matches: normalized.stats.matches + 1,
      wins: normalized.stats.wins + Number(mode === 'tdm' && winner === 'blue'),
      losses: normalized.stats.losses + Number(mode === 'tdm' && winner === 'red'),
      draws: normalized.stats.draws + Number(mode === 'tdm' && winner === 'draw'),
      kills: normalized.stats.kills + kills,
      deaths: normalized.stats.deaths + deaths,
      bestWave: Math.max(normalized.stats.bestWave, wave),
    },
  });

  const previousLevel = getProfileProgress(normalized).level;
  const nextLevel = getProfileProgress(nextProfile).level;
  return {
    profile: nextProfile,
    earnedXp,
    previousLevel,
    level: nextLevel,
    levelsGained: Math.max(0, nextLevel - previousLevel),
  };
}
