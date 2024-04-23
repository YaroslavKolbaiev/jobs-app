<script setup lang="ts">
import { useAuthStore } from "@/stores/auth";
import IconLogin from "../icons/IconLogin.vue";
import IconUser from "../icons/IconUser.vue";
import TogleTheme from "./TogleTheme.vue";

const useAuth = useAuthStore();
</script>

<template>
  <header class="header">
    <div class="flex-between-center container">
      <div class="logos flex-between-center">
        <RouterLink class="logo" :to="'/'">
          <img src="../../assets/logo.svg" alt="logo" />
        </RouterLink>

        <h1 class="title">Ultimate Job</h1>
      </div>

      <div class="buttons">
        <TogleTheme />

        <RouterLink v-if="useAuth.user" to="/post-job" class="button clickable">
          Post a Job
        </RouterLink>

        <RouterLink v-if="useAuth.user" to="/profile" class="login clickable">
          <IconUser />
        </RouterLink>

        <RouterLink v-else :to="'/login'" class="login clickable">
          <IconLogin />
        </RouterLink>
      </div>
    </div>
  </header>
</template>

<style scoped lang="scss">
@import "../../styles/mixins.scss";
@import "../../styles/buttons.scss";

.header {
  background-color: var(--header-bg);
}

.logos {
  gap: 10px;
}

.logo {
  display: flex;
  @include square_32;

  @include onTablet {
    @include square_48;
  }

  @include onDesktop {
    @include square_64;
  }

  & > img {
    border-radius: 50%;
  }
}

.buttons {
  display: flex;
  align-items: center;
  gap: 10px;
  @include onTablet {
    gap: 20px;
  }
}

.title {
  display: none;
  margin: 0;

  font-weight: 400;
  color: var(--header-text);

  @include onTablet {
    display: block;
  }
}

.login {
  @include square_32;
  display: flex;
  align-items: center;
  justify-content: center;

  @include onDesktop {
    @include square_48;
  }
}
</style>
