<script setup lang="ts">
import { computed } from "vue";
import { useRoute } from "vue-router";
const route = useRoute();

const isRegisterPage = computed(() => route.path === "/register");
</script>

<template>
  <div class="form__footer">
    <p>
      {{
        isRegisterPage ? "Already have an account?" : "Don't have an account?"
      }}
    </p>
    <RouterLink
      :to="isRegisterPage ? '/login' : '/register'"
      class="form__footer-link"
    >
      {{ isRegisterPage ? "Log In" : "Register" }}
    </RouterLink>
  </div>
</template>

<style scoped lang="scss">
@import "../../styles/form.scss";
</style>
