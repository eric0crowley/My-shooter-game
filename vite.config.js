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
  resolve: {
    // Use the separate WASM asset instead of the base64 compatibility bundle.
    // This keeps the navigation runtime smaller and lets Vite package the WASM
    // binary as an ordinary offline asset for Capacitor.
    alias: [
      { find: /^@recast-navigation\/wasm$/, replacement: '@recast-navigation/wasm/wasm' },
    ],
  },
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    chunkSizeWarningLimit: 600,
  },
});
