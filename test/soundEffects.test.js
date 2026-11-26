import test from 'node:test';
import assert from 'node:assert/strict';
import { SoundEffects } from '../src/SoundEffects.js';

test('master volume can be set before audio unlock and is clamped safely', () => {
  const sound = new SoundEffects();
  assert.equal(sound.masterVolume, 0.32);

  sound.setMasterVolume(0.74);
  assert.equal(sound.masterVolume, 0.74);

  sound.setMasterVolume(4);
  assert.equal(sound.masterVolume, 1);
  sound.setMasterVolume(-1);
  assert.equal(sound.masterVolume, 0);
  sound.setMasterVolume(Number.NaN);
  assert.equal(sound.masterVolume, 0.32);
});

test('a volume selected before unlock is applied to the created audio master gain', async () => {
  const previousWindow = globalThis.window;
  const previousFetch = globalThis.fetch;
  class FakeAudioContext {
    constructor() {
      this.state = 'running';
      this.sampleRate = 100;
      this.currentTime = 0;
      this.destination = {};
    }
    createGain() {
      return { gain: { value: 0, setTargetAtTime() {} }, connect() {} };
    }
    createBuffer(_channels, length) {
      return { getChannelData: () => new Float32Array(length) };
    }
    async decodeAudioData() { return {}; }
  }

  try {
    globalThis.window = { AudioContext: FakeAudioContext };
    globalThis.fetch = async () => ({
      ok: true,
      arrayBuffer: async () => new ArrayBuffer(0),
    });
    const sound = new SoundEffects();
    sound.setMasterVolume(0.81);
    await sound.unlock();
    await sound.samplesLoading;
    assert.equal(sound.master.gain.value, 0.81);
  } finally {
    if (previousWindow === undefined) delete globalThis.window;
    else globalThis.window = previousWindow;
    globalThis.fetch = previousFetch;
  }
});
