import { Capacitor, registerPlugin } from '@capacitor/core';

const NativeLan = registerPlugin('LanMultiplayer');
const DEFAULT_PORT = 24180;

export class LanTransport {
  constructor() {
    this.handles = [];
    this.role = null;
  }

  get available() {
    return Capacitor.isNativePlatform();
  }

  async listen(eventName, callback) {
    if (!this.available) return null;
    const handle = await NativeLan.addListener(eventName, callback);
    this.handles.push(handle);
    return handle;
  }

  async startHost(port = DEFAULT_PORT) {
    this.requireNative();
    const result = await NativeLan.startHost({ port });
    this.role = 'host';
    return result;
  }

  async connect(host, port = DEFAULT_PORT) {
    this.requireNative();
    const result = await NativeLan.connect({ host, port });
    this.role = 'client';
    return result;
  }

  async send(message) {
    this.requireNative();
    return NativeLan.send({ message });
  }

  async sendTo(peerId, message) {
    this.requireNative();
    return NativeLan.sendTo({ peerId, message });
  }

  async close(role = this.role) {
    if (!this.available || !role) return;
    try {
      if (role === 'host') await NativeLan.stopHost();
      else await NativeLan.disconnect();
    } finally {
      this.role = null;
    }
  }

  requireNative() {
    if (!this.available) {
      throw new Error('شبکهٔ محلی فقط در نسخهٔ نصب‌شدهٔ اندروید در دسترس است.');
    }
  }
}

export { DEFAULT_PORT };
