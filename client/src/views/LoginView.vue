<script setup lang="ts">
import useFetchData from '@/composables/useFetchData';
// import { validateEmail, validatePassword } from '@/utils';
import ErrorToast from '@/components/ErrorToast.vue';
import { login } from '@/api';
import { ref, watch } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const router = useRouter();

const useAuth = useAuthStore();

const email = ref('');
const password = ref('');

const { data, isLoading, error, doRequest } = useFetchData(() =>
  login(email.value, password.value)
);

watch(
  () => data.value,
  () => {
    if (data.value) {
      useAuth.login();

      router.push('/');
    }
  }
);
</script>

<template>
  <main>
    <div class="container">
      <form @submit.prevent="doRequest">
        <h2>Log in to your account</h2>
        <p v-if="isLoading">Loading....</p>
        <span>Please enter your details below to continue</span>
        <div class="search-wrapper">
          <input
            name="email"
            type="text"
            placeholder="Enter Your username"
            v-model="email"
            required
          />
        </div>
        <div class="search-wrapper">
          <input
            name="password"
            type="password"
            v-model="password"
            placeholder="Enter Your Password"
          />
        </div>
        <button :disabled="isLoading" class="button clickable" type="submit">
          Log In
        </button>
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
@import '../styles/mixins.scss';
@import '../styles/transitions/slide.scss';

form {
  background-color: var(--card-bg);
  box-shadow: 0 9px 18px rgba(37, 41, 49, 0.03);
  border-radius: 10px;
  padding: 40px;
  max-width: 480px;
  margin: 40px auto 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

input {
  box-sizing: border-box;
  width: 100%;
  border-radius: 40px;
  padding: 20px 20px 20px 40px;
  background: none;
  border: 1px solid var(--c-blue);
  transition: all 0.3s ease-in-out;
  font-size: 16px;
  color: var(--c-main-text);

  &::placeholder {
    color: var(--c-gray);
    opacity: 0.5;
  }

  &:focus {
    outline: none;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  &:hover {
    border-color: #1f7ace;
  }
}

button {
  border-radius: 40px;
  font-size: 18px;
  font-weight: 600;
  padding: 12px 16px;
}

span {
  margin-bottom: 10px;
}
</style>
