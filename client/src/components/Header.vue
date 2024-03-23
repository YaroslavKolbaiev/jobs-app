<script setup lang="ts">
import IconLogin from './icons/IconLogin.vue';
import IconUser from './icons/IconUser.vue';
import TogleTheme from './TogleTheme.vue';
</script>

<template>
  <header class="header">
    <div class="flex-between-center container">
      <div class="header__logos flex-between-center">
        <img class="logo" src="../assets/logo.svg" alt="logo" />
        <h1 class="title">Ultimate Job</h1>
      </div>
      <div class="header__buttons">
        <TogleTheme />
        <RouterLink v-if="true" :to="'#'" class="button clickable">
          Post a Job
        </RouterLink>
        <RouterLink v-if="false" :to="'#'" class="login clickable">
          <IconLogin />
        </RouterLink>
        <RouterLink v-if="true" :to="'#'" class="login clickable">
          <IconUser />
        </RouterLink>
      </div>
    </div>
  </header>
</template>

<style scoped lang="scss">
@import '../styles/mixins.scss';

.header {
  background-color: var(--header-bg);

  &__logos {
    gap: 10px;
  }

  &__buttons {
    display: flex;
    align-items: center;
    gap: 10px;
    @include onTablet {
      gap: 20px;
    }
  }
}

.title {
  display: none;
  margin: 0;
  font-family: Poppins, sans-serif;
  font-weight: 400;
  color: var(--header-text);

  @include onTablet {
    display: block;
  }
}

.logo {
  @include square_32;
  border-radius: 50%;

  @include onTablet {
    @include square_48;
  }

  @include onDesktop {
    @include square_64;
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
