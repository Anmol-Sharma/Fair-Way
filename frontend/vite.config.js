import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
// import { loadEnv } from 'vite'

// https://vite.dev/config/
export default defineConfig(({ command, mode }) => {
  // Load env file based on `mode` in the current working directory.
  // Set the third parameter to '' to load all env regardless of the `VITE_` prefix.
  // const env = loadEnv(mode, process.cwd(), '')

  return {
    plugins: [
      vue(),
    ],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      },
    },
    server: {
      host: '0.0.0.0',

      // Note:- Vite Proxy only works for the dev server and doesn't work at all with production `npm run build`
      //        so define the backend routes appropriately
      // proxy: {
      //   '/api': {
      //     target: env.VITE_API_URL,
      //     changeOrigin: true,
      //     secure: false,
      //     rewrite: path => path.replace(/^\/api/, ''),
      //   },
      // }
    }
  }//,
  // Make env variables available to your app
  // define: {
  //   'process.env': env
  // }
})
