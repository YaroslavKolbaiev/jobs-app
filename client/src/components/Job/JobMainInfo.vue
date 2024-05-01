<script setup lang="ts">
import { applyToJob } from "@/api/jobs";
import IconLocation from "@/components/icons/IconLocation.vue";
import IconLoader from "@/components/icons/IconLoader.vue";
import ErrorToast from "@/components/ErrorToast.vue";
import useFetchData from "@/hooks/useFetchData";
import type { MainInfoProps } from "@/types";
import { ref, watch } from "vue";

const { jobId, title, company, address, description, candidates } =
  defineProps<MainInfoProps>();

const reactiveCandidates = ref(candidates);

const { data, doRequest, isLoading, error } = useFetchData(() =>
  applyToJob(jobId)
);

watch(
  () => data.value,
  () => {
    if (data.value && typeof reactiveCandidates.value === "number") {
      reactiveCandidates.value += 1;
    }
  }
);
</script>

<template>
  <h1 class="mainInfo__title">
    {{ title }}
  </h1>

  <div class="mainInfo">
    <h2 class="mainInfo__name">
      {{ company }}
    </h2>
    <p class="mainInfo__adress">
      <IconLocation class="mainInfo__location" />
      <span>{{ address }}</span>
    </p>
  </div>

  <div class="mainInfo">
    <button
      @click="doRequest"
      class="button button--form"
      type="button"
      :disabled="isLoading"
    >
      <IconLoader v-if="isLoading" />
      <span v-else>Apply Now</span>
    </button>

    <span class="mainInfo__candidates">{{ reactiveCandidates }} Candidates have applied for this job</span>
  </div>

  <p class="mainInfo__description">
    <strong>Description:</strong>
    <br />
    {{ description }}
  </p>

  <transition name="slide">
    <ErrorToast
      v-if="error"
      :error="error?.message"
      @clear-error="error = null"
    />
  </transition>
</template>

<style scoped lang="scss">
@import "../../styles/mixins.scss";
@import "../../styles/buttons.scss";
@import "../../styles/transitions/slide.scss";

.mainInfo {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 20px;

  @include onTablet {
    flex-direction: row;
    align-items: center;
  }

  &__title {
    color: var(--c-main-text);
    margin: 0;
  }

  &__name {
    margin: 0;
    color: var(--c-blue);
  }

  &__adress {
    margin: 0;
    color: var(--c-gray);
    display: flex;
    align-items: center;
    font-size: 14px;
  }

  &__candidates {
    color: #228b22;
  }

  &__description {
    margin: 0;
    font-size: 14px;
    color: var(--c-main-text);

    & > strong {
      font-size: 20px;
    }
  }

  &__location {
    width: 24px;
    min-width: 24px;
    stroke: var(--c-main-text);
  }
}

.button {
  width: 170px;
}
</style>
