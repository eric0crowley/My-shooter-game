import test from 'node:test';
import assert from 'node:assert/strict';
import {
  DEFAULT_GAME_SETTINGS,
  GAME_SETTINGS_KEY,
  loadGameSettings,
  sanitizeGameSettings,
  saveGameSettings,
} from '../src/GameSettings.js';

function memoryStorage(initial = {}) {
  const values = new Map(Object.entries(initial));
  return {
    getItem(key) { return values.get(key) ?? null; },
    setItem(key, value) { values.set(key, String(value)); },
  };
}

test('settings load usable defaults when there is no browser storage', () => {
  assert.deepEqual(loadGameSettings(null), DEFAULT_GAME_SETTINGS);
});

test('settings are clamped to safe camera and volume ranges', () => {
  assert.deepEqual(sanitizeGameSettings({
    lookSensitivity: 99,
    masterVolume: -2,
    fieldOfView: 120,
    unused: true,
  }), {
    lookSensitivity: 2.5,
    masterVolume: 0,
    fieldOfView: 100,
    graphicsQuality: 'auto',
  });
});

test('graphics quality accepts only supported presets', () => {
  assert.equal(
    sanitizeGameSettings({ graphicsQuality: 'quality' }).graphicsQuality,
    'quality',
  );
  assert.equal(
    sanitizeGameSettings({ graphicsQuality: 'ultra' }).graphicsQuality,
    'auto',
  );
});

test('settings round-trip through persistent storage and ignore malformed values', () => {
  const storage = memoryStorage();
  const saved = saveGameSettings({ lookSensitivity: 1.4, masterVolume: 0.6, fieldOfView: 82.4 }, storage);
  assert.deepEqual(saved, {
    lookSensitivity: 1.4,
    masterVolume: 0.6,
    fieldOfView: 82,
    graphicsQuality: 'auto',
  });
  assert.deepEqual(loadGameSettings(storage), saved);

  storage.setItem(GAME_SETTINGS_KEY, '{not-json');
  assert.deepEqual(loadGameSettings(storage), DEFAULT_GAME_SETTINGS);
});

test('settings remain usable when a WebView denies storage access', () => {
  const deniedStorage = {
    getItem() { throw new Error('storage disabled'); },
    setItem() { throw new Error('storage disabled'); },
  };
  assert.deepEqual(loadGameSettings(deniedStorage), DEFAULT_GAME_SETTINGS);
  assert.deepEqual(saveGameSettings({ masterVolume: 0.1 }, deniedStorage), {
    ...DEFAULT_GAME_SETTINGS,
    masterVolume: 0.1,
  });
});
