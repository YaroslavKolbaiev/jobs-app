<script setup lang="ts">
import { RouterView } from 'vue-router';
import Header from './components/Header/Header.vue';
import { useAuthStore } from './stores/auth';

const authStore = useAuthStore();
function getCookie(id: string) {
  const value = document.cookie.match('(^|;)?' + id + '=([^;]*)(;|$)');
  return value ? unescape(value[2]) : null;
}
</script>

<template>
  <Header />
  <RouterView />
  <footer>Footer</footer>
</template>

<style scoped></style>
