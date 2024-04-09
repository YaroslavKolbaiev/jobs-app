<script setup lang="ts">
import useFetchData from '@/hooks/useFetchData';
import ErrorToast from '@/components/ErrorToast.vue';
import IconLoader from '@/components/icons/IconLoader.vue';
import ShowPassword from '@/components/auth/ShowPassword.vue';
import FormFooter from '@/components/auth/FormFooter.vue';
import { login } from '@/api/auth';
import { ref, watch } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const router = useRouter();

const useAuth = useAuthStore();

const email = ref('');
const password = ref('');
const showPassword = ref(false);

const { data, isLoading, error, doRequest } = useFetchData(() =>
  login(email.value, password.value)
);

watch(
  () => data.value,
  () => {
    if (data.value) {
      useAuth.login(data.value.data);

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
            placeholder="Enter Your email"
            v-model="email"
            required
          />
        </div>

        <div class="form__wrapper">
          <input
            class="form__input"
            name="password"
            :type="showPassword ? 'text' : 'password'"
            v-model="password"
            placeholder="Enter Your password"
          />
          <ShowPassword
            @click="showPassword = !showPassword"
            :show="showPassword"
          />
        </div>

        <button
          :disabled="isLoading"
          class="button button--form clickable"
          type="submit"
        >
          <IconLoader v-if="isLoading" />
          <span v-else>Log In</span>
        </button>

        <FormFooter />
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
</style>
