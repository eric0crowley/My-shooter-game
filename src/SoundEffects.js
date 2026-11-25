export class SoundEffects {
  constructor() {
    this.context = null;
    this.master = null;
    this.noiseBuffer = null;
  }

  async unlock() {
    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    if (!AudioContextClass) return false;
    if (!this.context) {
      this.context = new AudioContextClass();
      this.master = this.context.createGain();
      this.master.gain.value = 0.32;
      this.master.connect(this.context.destination);
      this.noiseBuffer = this.context.createBuffer(1, Math.floor(this.context.sampleRate * 0.22), this.context.sampleRate);
      const samples = this.noiseBuffer.getChannelData(0);
      for (let i = 0; i < samples.length; i++) samples[i] = Math.random() * 2 - 1;
    }
    if (this.context.state === 'suspended') await this.context.resume();
    return true;
  }

  tone(frequency, duration, type = 'sine', volume = 0.12, endFrequency = frequency) {
    if (!this.context || !this.master) return;
    const now = this.context.currentTime;
    const oscillator = this.context.createOscillator();
    const gain = this.context.createGain();
    oscillator.type = type;
    oscillator.frequency.setValueAtTime(Math.max(20, frequency), now);
    oscillator.frequency.exponentialRampToValueAtTime(Math.max(20, endFrequency), now + duration);
    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.exponentialRampToValueAtTime(Math.max(0.0002, volume), now + 0.008);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);
    oscillator.connect(gain);
    gain.connect(this.master);
    oscillator.start(now);
    oscillator.stop(now + duration + 0.012);
  }

  noise(duration, volume, cutoff = 1800) {
    if (!this.context || !this.master || !this.noiseBuffer) return;
    const now = this.context.currentTime;
    const source = this.context.createBufferSource();
    const filter = this.context.createBiquadFilter();
    const gain = this.context.createGain();
    source.buffer = this.noiseBuffer;
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(cutoff, now);
    gain.gain.setValueAtTime(Math.max(0.0001, volume), now);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);
    source.connect(filter);
    filter.connect(gain);
    gain.connect(this.master);
    source.start(now);
    source.stop(now + duration);
  }

  shot(weaponId) {
    if (!this.context) return;
    const isShotgun = weaponId === 'shotgun';
    const isPistol = weaponId === 'pistol';
    this.tone(isShotgun ? 88 : (isPistol ? 145 : 112), isShotgun ? 0.19 : 0.12, 'sawtooth', isShotgun ? 0.2 : 0.12, isShotgun ? 38 : 62);
    this.noise(isShotgun ? 0.17 : 0.1, isShotgun ? 0.22 : (isPistol ? 0.14 : 0.09), isShotgun ? 1200 : 2600);
  }

  hit() {
    this.tone(1080, 0.045, 'sine', 0.08, 740);
    this.tone(1460, 0.055, 'sine', 0.045, 1180);
  }

  damage() {
    this.tone(92, 0.24, 'sawtooth', 0.14, 42);
    this.noise(0.18, 0.045, 420);
  }

  reload() {
    this.tone(420, 0.035, 'square', 0.035, 260);
    window.setTimeout(() => this.tone(620, 0.055, 'square', 0.04, 380), 160);
  }

  waveStart(wave) {
    const base = wave > 1 ? 350 : 260;
    this.tone(base, 0.14, 'triangle', 0.09, base * 1.5);
    window.setTimeout(() => this.tone(base * 1.5, 0.19, 'triangle', 0.075, base * 2), 110);
  }

  death() {
    this.tone(190, 0.42, 'sawtooth', 0.12, 48);
  }
}
