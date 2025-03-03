const colors = require('tailwindcss/colors')

module.exports = {
  content: [
    'src/**/*.html',
  ],
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    colors: {
      ...colors,
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}

