<script setup lang="ts">
import useFetchData from '@/composables/useFetchData';
import ErrorToast from '@/components/ErrorToast.vue';
import IconLoader from '@/components/icons/IconLoader.vue';
import IconEye from '@/components/icons/IconEye.vue';
import IconEyeX from '@/components/icons/IconEyeX.vue';
import { login } from '@/api/auth';
import { ref, watch } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const router = useRouter();

const useAuth = useAuthStore();

const email = ref('');
const password = ref('');
const showPasswprd = ref(false);

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
      <form class="form" @submit.prevent="doRequest">
        <h2>Log in to your account</h2>

        <span>Please enter your details below to continue</span>

        <div class="form__wrapper">
          <input
            class="form__input"
            name="email"
            type="text"
            placeholder="Enter Your E-Mail"
            v-model="email"
            required
          />
        </div>

        <div class="form__wrapper">
          <input
            class="form__input"
            name="password"
            :type="showPasswprd ? 'text' : 'password'"
            v-model="password"
            placeholder="Enter Your Password"
          />
          <button
            class="show-password form__icon form__icon--password"
            type="button"
            @click="showPasswprd = !showPasswprd"
          >
            <IconEye v-if="!showPasswprd" />
            <IconEyeX v-else />
          </button>
        </div>

        <button
          :disabled="isLoading"
          class="button button--form clickable"
          type="submit"
        >
          <IconLoader v-if="isLoading" />
          <span v-else>Log In</span>
        </button>

        <div class="no-account">
          <p>Don't have an account?</p>
          <RouterLink to="/register" class="register-link">
            Sign Up
          </RouterLink>
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
@import '../styles/transitions/slide.scss';
@import '../styles/form.scss';
@import '../styles/buttons.scss';

h2 {
  margin-top: 0;
}

.show-password {
  border: none;
  background: none;
  padding: 0;
  display: flex;
  cursor: pointer;
}

.no-account {
  display: flex;
  align-items: center;
  gap: 10px;
}

.register-link {
  color: var(--c-blue);
  text-decoration: none;
}
</style>
