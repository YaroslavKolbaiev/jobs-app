<script setup lang="ts">
import { RouterView } from "vue-router";
import Header from "./components/Header/Header.vue";
import Footer from "./components/Footer/Footer.vue";
import { onMounted } from "vue";
import { getUser } from "./api/auth";
import { useAuthStore } from "./stores/auth";

const useAuth = useAuthStore();

onMounted(async () => {
  const { data } = await getUser();

  if (data) {
    useAuth.login(data);
  }
});
</script>

<template>
  <Header />
  <RouterView />
  <Footer />
</template>

<style scoped></style>
