<script setup lang="ts">
import { RouterView } from 'vue-router';
import Header from './components/Header/Header.vue';
import { useAuthStore } from './stores/auth';

const authStore = useAuthStore();

</script>

<template>
  <Header />
  <RouterView />
  <footer>Footer</footer>
</template>

<style scoped></style>
