<script setup lang="ts">
import useFetchData from "@/hooks/useFetchData";
import { reactive, ref } from "vue";
import { register } from "@/api/auth";
import IconLoader from "@/components/icons/IconLoader.vue";
import ErrorToast from "@/components/ErrorToast.vue";
import ShowPassword from "@/components/auth/ShowPassword.vue";
import TermsAndConditions from "@/components/auth/TermsAndConditions.vue";
import ModalNote from "@/components/auth/ModalNote.vue";
import FormFooter from "@/components/auth/FormFooter.vue";
import { InputNames } from "@/enums";

const userCredentials = reactive({
  email: "",
  password: "",
  confirmPassword: "",
  username: "",
  first_name: "",
  last_name: "",
});

const isAgree = ref(false);
const showPassword = ref(false);
const showConfirmPassword = ref(false);

const { data, isLoading, error, doRequest } = useFetchData(() =>
  register(userCredentials)
);
</script>

<template>
  <main>
    <div class="container">
      <form class="form" action="" @submit.prevent="doRequest">
        <h2>Register to <strong>Ultimate Job</strong></h2>

        <div
          v-for="input in Object.values(InputNames)"
          :key="input"
          class="form__wrapper"
        >
          <input
            class="form__input"
            :name="input"
            type="text"
            :placeholder="`Enter Your ${input.replace('_', ' ')}`"
            v-model="userCredentials[input]"
            required
          />
        </div>

        <div class="form__wrapper">
          <input
            class="form__input"
            name="password"
            :type="showPassword ? 'text' : 'password'"
            placeholder="Enter Your password"
            v-model="userCredentials.password"
            required
          />
          <ShowPassword
            @click="showPassword = !showPassword"
            :show="showPassword"
          />
        </div>

        <div class="form__wrapper">
          <input
            class="form__input"
            name="confirmPassword"
            :type="showConfirmPassword ? 'text' : 'password'"
            placeholder="Confirm Your password"
            v-model="userCredentials.confirmPassword"
            required
          />
          <ShowPassword
            @click="showConfirmPassword = !showConfirmPassword"
            :show="showConfirmPassword"
          />
        </div>

        <TermsAndConditions @terms-accepted="isAgree = !isAgree" />

        <button
          :disabled="isLoading || !isAgree"
          class="button button--form"
          :class="{
            clickable: isAgree,
            button__disabled: !isAgree,
          }"
          type="submit"
        >
          <IconLoader v-if="isLoading" />
          <span v-else>Register</span>
        </button>

        <FormFooter />
      </form>
    </div>
  </main>
  <transition name="fade">
    <ModalNote v-if="data" />
  </transition>

  <transition name="slide">
    <ErrorToast
      v-if="error"
      :error="error?.message"
      @clear-error="error = null"
    />
  </transition>
</template>

<style scoped lang="scss">
@import "../styles/transitions/slide.scss";
@import "../styles/transitions/fade.scss";
@import "../styles/form.scss";
@import "../styles/buttons.scss";

strong {
  color: var(--c-blue);
}
</style>
