<script setup lang="ts">
import ErrorToast from "@/components/ErrorToast.vue";
import UserJobs from "@/components/Job/UserJobs.vue";
import LogOutButton from "@/components/auth/LogOutButton.vue";
import UploadResume from "@/components/auth/UploadResume.vue";
import { useAuthStore } from "@/stores/auth";
import { ref, type Ref } from "vue";
import { userJobs, appliedJobs } from "@/api/jobs";
import { JobsByUser } from "@/enums";

const AMAZON_URL = import.meta.env.VITE_AMAZON_URL;

const useAuth = useAuthStore();

const error = ref<Error | null>(null);

const onErrorEmited = (err: Ref) => {
  error.value = err.value;
};
</script>

<template>
  <main>
    <div class="container grid">
      <div class="form grid__item--1-5">
        <p>Profile</p>

        <h2>Welcome, {{ useAuth.user?.username }}</h2>

        <a
          v-if="useAuth.user?.resume"
          :href="`${AMAZON_URL}/${useAuth.user?.resume}`"
          target="_blank"
        >
          Download Resume
        </a>

        <LogOutButton @error-emited="onErrorEmited" />
      </div>

      <UserJobs
        @error-emited="onErrorEmited"
        :call-back="userJobs"
        :users-jobs="JobsByUser.Created"
      />

      <UploadResume @error-emited="onErrorEmited" />

      <UserJobs
        @error-emited="onErrorEmited"
        :call-back="appliedJobs"
        :users-jobs="JobsByUser.Applied"
      />
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
@import "../styles/gridFlex.scss";
@import "../styles/buttons.scss";
@import "../styles/transitions/slide.scss";
@import "../styles//job.scss";

.form {
  margin: 0;
  margin-bottom: 10px;
  max-width: 100%;

  @include onDesktop {
    margin-bottom: 0;
  }
}

.profile-buttons {
  display: flex;
  gap: 10px;
}

p {
  font-size: 24px;
}

a {
  color: var(--c-blue);
  margin-bottom: 20px;
}
</style>
