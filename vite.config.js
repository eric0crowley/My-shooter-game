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
    // Keep Three.js cacheable separately from the game shell so later UI/gameplay
    // updates do not force every device to download the rendering runtime again.
    rolldownOptions: {
      output: {
        codeSplitting: {
          minSize: 20000,
          groups: [
            { name: 'three-vendor', test: /node_modules\/three\// },
          ],
        },
      },
    },
  },
});
