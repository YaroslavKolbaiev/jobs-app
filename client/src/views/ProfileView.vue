<script setup lang="ts">
import ErrorToast from "@/components/ErrorToast.vue";
import useFetchData from "@/hooks/useFetchData";
import { useAuthStore } from "@/stores/auth";
import { logout } from "@/api/auth";

const useAuth = useAuthStore();

const onLogout = async () => {
  logout();
  useAuth.logout();
};

const { isLoading, error, doRequest } = useFetchData(onLogout);
</script>

<template>
  <main>
    <div class="container">
      <form @submit.prevent="doRequest" class="form">
        <p>Profile</p>
        <h2>Welcome, {{ useAuth.user?.username }}</h2>
        <div>
          <button type="button" class="button">Upload resume</button>
          <button type="submit" class="button button--logout">Log out</button>
        </div>
      </form>
    </div>
  </main>
  <transition name="slide">
    <ErrorToast
      v-if="error"
      :error="error?.message"
      @clear-error="error = null"
    />
  </transition>
</template>

<style scoped lang="scss">
@import "../styles/form.scss";
@import "../styles/buttons.scss";
@import "../styles/gridFlex.scss";

button {
  margin-right: 20px;
  margin-bottom: 10px;

  &:last-child {
    margin-right: 0;
    margin-bottom: 0;
  }
}

p {
  font-size: 24px;
}
</style>
