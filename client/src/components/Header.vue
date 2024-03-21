<script setup lang="ts">
import { RouterLink } from 'vue-router';
</script>

<template>
  <header class="header">
    <div class="wrapper">
      <img class="logo" src="../assets/logo.svg" alt="logo" />
      <div class="links">
        <RouterLink :to="'#'" class="link"> Post a Job </RouterLink>
        <RouterLink :to="'#'" class="link"> Login </RouterLink>
      </div>
    </div>
  </header>
</template>

<style scoped lang="scss">
@import '../styles/mixins.scss';
@import '../styles/vars.scss';

.header {
  max-width: 1440px;
  margin: 0 auto;
  padding: 20px 40px;
  background-color: #2c2c2c;
}

.wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  width: 32px;
  height: 32px;
  border-radius: 50%;

  @include onTablet {
    width: 48px;
    height: 48px;
  }

  @include onDesktop {
    width: 64px;
    height: 64px;
  }
}

.links {
  display: flex;
  gap: 10px;
  @include onTablet {
    gap: 20px;
  }
}

.link {
  background-color: #2060f6;
  padding: 8px 10px;
  font-family: Poppins, sans-serif;
  font-size: 14px;
  font-weight: 400;
  text-decoration: none;
  border-radius: 10px;
  transition: background-color 200ms;
  color: $c-white;

  @include onTablet {
    font-size: 18px;
    font-weight: 600;
    padding: 12px 16px;
  }

  &:hover {
    background-color: #1a4fc9;
  }

  &:active {
    transform: scale(0.9);
  }
}
</style>
