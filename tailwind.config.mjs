/** @type {import('tailwindcss').Config} */
/** Panun Kaergar logo blue: #202048 */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#ededf0',
          100: '#dbdbe2',
          200: '#b8b8c4',
          300: '#9494a7',
          400: '#70708a',
          500: '#4d4d6d',
          600: '#202048',
          700: '#1b1b3d',
          800: '#161632',
          900: '#121228',
          950: '#0d0d1e',
        },
        accent: {
          DEFAULT: '#e8b818',
          dark: '#c49a10',
        },
        whatsapp: {
          DEFAULT: '#25D366',
          dark: '#128C7E',
        },
      },
      fontFamily: {
        sans: ['system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
        inter: ['"Inter Variable"', 'Inter', 'system-ui', 'sans-serif'],
      },
      keyframes: {
        'fade-up': {
          '0%': { opacity: '0', transform: 'translateY(16px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-8px)' },
        },
        'blob-drift': {
          '0%, 100%': { transform: 'translate(0, 0) scale(1)' },
          '33%': { transform: 'translate(12px, -16px) scale(1.05)' },
          '66%': { transform: 'translate(-8px, 8px) scale(0.95)' },
        },
      },
      animation: {
        'fade-up': 'fade-up 0.6s ease-out both',
        float: 'float 5s ease-in-out infinite',
        'blob-drift': 'blob-drift 12s ease-in-out infinite',
      },
    },
  },
};
