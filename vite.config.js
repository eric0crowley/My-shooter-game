import { defineConfig } from 'vite';

// base: './' makes asset paths relative so the built site can be wrapped
// into a Capacitor Android app (file:// or bundled webview) without a server.
export default defineConfig({
  base: './',
  server: {
    host: true,
    port: 5173,
    strictPort: false,
    // Allow the Arena preview proxy host (and any host) during dev.
    allowedHosts: true,
  },
  preview: {
    host: true,
    port: 4173,
    allowedHosts: true,
  },
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    // Three.js is intentionally bundled as a single offline-friendly chunk;
    // the production bundle is about 130 kB when gzip-compressed.
    chunkSizeWarningLimit: 600,
  },
});
