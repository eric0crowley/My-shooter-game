export const GAME_SETTINGS_KEY = 'rage-of-fight.settings.v1';

export const DEFAULT_GAME_SETTINGS = Object.freeze({
  lookSensitivity: 1,
  masterVolume: 0.32,
  fieldOfView: 75,
  graphicsQuality: 'auto',
});

const SETTINGS_RANGES = Object.freeze({
  lookSensitivity: [0.5, 2.5],
  masterVolume: [0, 1],
  fieldOfView: [60, 100],
});
const GRAPHICS_QUALITIES = new Set(['auto', 'performance', 'quality']);

function getStorage(storage) {
  if (storage !== undefined) return storage;
  try {
    return globalThis.localStorage || null;
  } catch {
    return null;
  }
}

function clampSetting(value, key) {
  const fallback = DEFAULT_GAME_SETTINGS[key];
  const [minimum, maximum] = SETTINGS_RANGES[key];
  if (value === null || value === undefined || value === '') return fallback;
  const numericValue = Number(value);
  return Number.isFinite(numericValue)
    ? Math.min(maximum, Math.max(minimum, numericValue))
    : fallback;
}

export function sanitizeGameSettings(settings = {}) {
  const source = settings && typeof settings === 'object' ? settings : {};
  return {
    lookSensitivity: clampSetting(source.lookSensitivity, 'lookSensitivity'),
    masterVolume: clampSetting(source.masterVolume, 'masterVolume'),
    fieldOfView: Math.round(clampSetting(source.fieldOfView, 'fieldOfView')),
    graphicsQuality: GRAPHICS_QUALITIES.has(source.graphicsQuality)
      ? source.graphicsQuality
      : DEFAULT_GAME_SETTINGS.graphicsQuality,
  };
}

export function loadGameSettings(storage) {
  try {
    const raw = getStorage(storage)?.getItem(GAME_SETTINGS_KEY);
    if (!raw) return { ...DEFAULT_GAME_SETTINGS };
    return sanitizeGameSettings(JSON.parse(raw));
  } catch {
    return { ...DEFAULT_GAME_SETTINGS };
  }
}

export function saveGameSettings(settings, storage) {
  const normalized = sanitizeGameSettings(settings);
  try {
    getStorage(storage)?.setItem(GAME_SETTINGS_KEY, JSON.stringify(normalized));
  } catch {
    // Private browsing and some WebViews can disable storage; settings still
    // apply in memory for the current session.
  }
  return normalized;
}
