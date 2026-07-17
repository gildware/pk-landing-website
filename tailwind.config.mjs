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
        figtree: ['Figtree', 'system-ui', 'sans-serif'],
      },
      transitionTimingFunction: {
        smooth: 'cubic-bezier(0.16, 1, 0.3, 1)',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        'blob-drift': {
          '0%, 100%': { transform: 'translate(0, 0) scale(1)' },
          '33%': { transform: 'translate(16px, -20px) scale(1.06)' },
          '66%': { transform: 'translate(-12px, 12px) scale(0.94)' },
        },
        shimmer: {
          '0%': { backgroundPosition: '-200% 0' },
          '100%': { backgroundPosition: '200% 0' },
        },
      },
      animation: {
        float: 'float 6s ease-in-out infinite',
        'blob-drift': 'blob-drift 14s ease-in-out infinite',
        shimmer: 'shimmer 2.5s linear infinite',
      },
    },
  },
};
