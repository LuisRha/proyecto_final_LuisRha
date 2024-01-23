
import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig({
   root: './app/vue',
   plugins: [
      vue(),
      vueJsx(),
   ],
   resolve: {
      alias: {
         '@': fileURLToPath(new URL('./app/vue/src', import.meta.url))
      }
   },
   // optimizeDeps: {
   //    include: ['vue', 'vue-router'], // Aquí incluimos las dependencias que podrían no ser detectadas automáticamente
   // },
})