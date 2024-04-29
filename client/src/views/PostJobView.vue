<script setup lang="ts">
import { JobInputNames } from "@/enums";
import { reactive } from "vue";
import IconLoader from "@/components/icons/IconLoader.vue";
import useFetchData from "@/hooks/useFetchData";
import { postJob } from "@/api/jobs";
import { JobType, Education, Industry } from "@/enums";
import NewJobSelect from "@/components/Job/NewJobSelect.vue";
import ErrorToast from "../components/ErrorToast.vue";
import { useRouter } from "vue-router";

const router = useRouter();

const newJob = reactive({
  title: "",
  description: "",
  email: "",
  address: "",
  salary: null,
  position: null,
  company: "",
  jobType: "",
  education: "",
  industry: "",
  experience: "",
});

const onSubmit = async () => {
  await postJob(newJob);
  router.push("/");
};

const { isLoading, error, doRequest } = useFetchData(onSubmit);
</script>

<template>
  <main>
    <div class="container">
      <form @submit.prevent="doRequest" class="form grid">
        <h2 class="grid__item--1-12">
          Create new job
        </h2>

        <div
          v-for="(input, index) in Object.values(JobInputNames)"
          :key="input"
          :class="`grid__item--${index % 2 === 0 ? '1-6' : '7-12'}`"
        >
          <input
            class="form__input"
            :name="input"
            :type="typeof newJob[input] === 'string' ? 'text' : 'number'"
            :placeholder="`${input.replace('_', ' ')}`"
            v-model="newJob[input]"
            required
          />
        </div>

        <NewJobSelect
          @emit-select="(value) => (newJob.jobType = value)"
          :options="Object.values(JobType)"
          :name="'Job Type'"
          class="grid__item--1-6 form__input"
        />

        <NewJobSelect
          @emit-select="(value) => (newJob.education = value)"
          :options="Object.values(Education)"
          :name="'Education Level'"
          class="grid__item--7-12 form__input"
        />

        <NewJobSelect
          @emit-select="(value) => (newJob.industry = value)"
          :options="Object.values(Industry)"
          :name="'Industry'"
          class="grid__item--1-6 form__input"
        />

        <button
          :disabled="isLoading"
          type="submit"
          class="button button--form grid__item--7-12"
        >
          <IconLoader v-if="isLoading" />
          <span v-else>Submit</span>
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
@import "../styles/form.scss";
@import "../styles/gridFlex.scss";
@import "../styles/buttons.scss";
@import "../styles/transitions/slide.scss";

.form {
  max-width: 100%;
}

select {
  appearance: none;
  cursor: pointer;
}
</style>
