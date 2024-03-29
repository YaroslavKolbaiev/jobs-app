/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution');

module.exports = {
  root: true,
  extends: [
    'plugin:vue/strongly-recommended',
    'eslint:recommended',
    '@vue/eslint-config-typescript',
    '@vue/typescript/recommended',
  ],
  parserOptions: {
    ecmaVersion: 'latest',
  },
  rules: {
    'vue/html-self-closing': 'off',
    'vue/no-use-v-if-with-v-for': 'off',
    'vue/multi-word-component-names': [
      'error',
      {
        ignores: ['Header', 'About', 'Map'],
      },
    ],
    'vue/no-multiple-template-root': 'off',
    'vue/max-attributes-per-line': [
      'warn',
      {
        singleline: {
          max: 3,
        },
        multiline: {
          max: 1,
        },
      },
    ],
  },
};
