<script setup lang="ts">
import JobMainInfo from '@/components/Job/JobMainInfo.vue';
import ErrorToast from '@/components/ErrorToast.vue';
import JobDetails from '@/components/Job/JobDetails.vue';
import JobNote from '@/components/Job/JobNote.vue';
import JobNotFound from '@/components/Job/JobNotFound.vue';
import { useRoute } from 'vue-router';
import { getJob } from '@/api';
import useFetchData from '@/composables/useFetchData';
import type { GetJobResponse } from '@/types';
import { computed } from 'vue';

const route = useRoute();
const jobId = route.params.id as string;

const { data, doRequest, isLoading, error } = useFetchData<GetJobResponse>(() =>
  getJob(jobId)
);

doRequest();

const mainInfoProps = computed(() => {
  const job = data.value?.job;

  return {
    title: job?.title,
    company: job?.company,
    address: job?.address,
    candidates: data.value?.candidates,
    description: job?.description,
  };
});

const jobDetailsProps = computed(() => {
  const job = data.value?.job;

  return {
    email: job?.email,
    createdAt: job?.created_at,
    lastDate: job?.lastDate,
  };
});

const isExpired = computed(() => {
  const job = data.value?.job;

  const isExpired = new Date(job?.lastDate as string) < new Date();

  return isExpired;
});
</script>
<template>
  <main>
    <div v-if="isLoading" class="container">Loading....</div>
    <div v-if="!error && !isLoading" class="container grid">
      <div class="job grid__item--1-8">
        <JobMainInfo v-bind="mainInfoProps" />
      </div>
      <div class="details grid__item--9-12">
        <JobDetails v-bind="jobDetailsProps" class="job" />
        <JobNote v-if="!isExpired" class="job note" />
      </div>
    </div>
    <JobNotFound v-if="error" />
  </main>
  <ErrorToast v-if="error" :error="error?.message" />
</template>

<style scoped lang="scss">
@import '../styles/mixins.scss';

.job {
  background-color: var(--card-bg);
  padding: 20px;
  border-radius: 10px;
  font-family: Poppins, sans-serif;
  flex-grow: 1;
  width: 100%;
  box-sizing: border-box;
}

.details {
  display: flex;
  gap: 20px;
  margin-top: 20px;
  flex-direction: column;

  @include onTablet {
    flex-direction: row;
  }

  @include onDesktop {
    flex-direction: column;
    margin: 0;
  }
}

.note {
  background-color: rgba(255, 127, 127, 0.6);
}
</style>
