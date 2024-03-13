/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./App.{js,jsx,ts,tsx}", "./app/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {},
    colors: {
      "magnetic-grey": "#eae4ef",
      "mint-green": "#c0ffd0",
      "money-green": "#009933",
      "forest-green": "#00661F",
      "magnetic-plum": "#32004c",
    },
  },
  plugins: [],
};