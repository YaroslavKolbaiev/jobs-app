<script setup lang="ts">
import { getJobs } from '../api';
import type { GetJobsResponse } from '@/types';
import CardSkeleton from './skeletones/CardSkeleton.vue';
import JobCard from './JobCard.vue';
import ErrorToast from './ErrorToast.vue';
import useFetchData from '../composables/useFetchData';

const { data, doRequest, isLoading, error } = useFetchData<GetJobsResponse>(
  () => getJobs()
);

doRequest();
</script>

<template>
  <div class="jobs grid__item--5-12">
    <CardSkeleton
      v-if="isLoading"
      v-for="index in 4"
      :key="`id-${index}`"
      :class="{ elevated: index % 2 === 0 }"
    />
    <JobCard
      v-for="({ id, title, description, industry }, index) in data?.jobs"
      :key="id"
      :id="id"
      :title="title"
      :description="description"
      :industry="industry"
      :class="{ elevated: index % 2 != 0 }"
    />
  </div>
  <ErrorToast v-if="error" :error="error?.message" />
</template>

<style scoped lang="scss">
@import '../styles/mixins.scss';

.jobs {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: Poppins, sans-serif;
  gap: var(--jobs-gap);

  @include onTablet {
    flex-direction: row;
    flex-wrap: wrap;
  }
}

.elevated {
  @include onTablet {
    transform: translateY(-50%);
  }
  @include onDesktop {
    transform: translateY(-20%);
  }
}
</style>
