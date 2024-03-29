<script setup lang="ts">
import JobMainInfo from '@/components/Job/JobMainInfo.vue';
import ErrorToast from '@/components/ErrorToast.vue';
import JobDetails from '@/components/Job/JobDetails.vue';
import JobInfoTable from '@/components/Job/JobInfoTable.vue';
import JobNote from '@/components/Job/JobNote.vue';
import Map from '@/components/Map.vue';
import JobViewSkeleton from '@/components/skeletones/JobViewSkeleton.vue';
import { useRoute } from 'vue-router';
import { getJob } from '@/api';
import useFetchData from '@/composables/useFetchData';
import { useComputed } from '@/composables/useComputed';
import type { GetJobResponse } from '@/types';

const route = useRoute();
const jobId = route.params.id as string;

const { data, doRequest, isLoading, error } = useFetchData<GetJobResponse>(() =>
  getJob(jobId)
);

doRequest();

const { mainInfoProps, jobDetailsProps, jobInfoTableProps, isExpired } =
  useComputed(data);
</script>
<template>
  <main>
    <JobViewSkeleton
      :is-expired="isExpired"
      v-if="isLoading"
      class="container grid"
    />
    <div v-if="!error && !isLoading" class="container grid">
      <div class="job grid__item--1-8">
        <JobMainInfo v-bind="mainInfoProps" />
        <JobInfoTable v-bind="jobInfoTableProps" />
      </div>
      <div class="grid__item--9-12">
        <div class="job-details">
          <JobDetails v-bind="jobDetailsProps" class="job" />
          <JobNote v-if="!isExpired" class="job note" />
        </div>
        <Map :point="data?.job.point" />
      </div>
    </div>
  </main>
  <ErrorToast v-if="error" :error="error?.message" />
</template>

<style scoped lang="scss">
@import '../styles/mixins.scss';
</style>
