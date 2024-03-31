<script setup lang="ts">
import JobInSearch from '@/components/Search/JobInSearch.vue';
import ErrorToast from '@/components/ErrorToast.vue';
import NoSearchResults from '@/components/Search/NoSearchResults.vue';
import SerchViewSkeleton from '@/components/skeletones/SerchViewSkeleton.vue';
import Pagination from '@/components/Pagination.vue';
import { getJobs } from '@/api';
import useFetchData from '@/composables/useFetchData';
import type { GetJobsResponse, QueryParams } from '@/types';
import { useRoute } from 'vue-router';
import { useComputedPage } from '@/composables/useComputed';

const route = useRoute();
const query = route.query as unknown as QueryParams<string>;

const keyword = query.keyword;
const location = query.location;

const { page } = useComputedPage();

const { data, doRequest, isLoading, error } = useFetchData<GetJobsResponse>(
  () => getJobs('1', { keyword, location })
);

doRequest();
</script>

<template>
  <main>
    <div class="container">
      <h2>Results for:</h2>
      <span>{{ keyword }} jobs in {{ location }}</span>
      <SerchViewSkeleton v-if="isLoading" />
      <JobInSearch v-if="!isLoading" :jobs="data?.jobs" />
      <NoSearchResults v-if="!data?.jobs.length && !isLoading" />
      <Pagination
        :key="`${data?.total_jobs}-${page}-${data?.jobs_per_page}`"
        :total_jobs="data?.total_jobs"
        :jobs_per_page="data?.jobs_per_page"
        :page="page"
      />
    </div>
  </main>
  <ErrorToast v-if="error" :error="error?.message" />
</template>

<style scoped lang="scss">
@import '../styles/mixins.scss';

h2 {
  display: inline;
  color: var(--c-main-text);
  margin-right: 10px;
  font-size: 16px;

  @include onTablet {
    font-size: 22px;
  }
}

span {
  color: var(--c-blue);
}
</style>
