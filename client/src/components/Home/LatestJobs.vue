<script setup lang="ts">
import { getJobs } from '../../api';
import type { GetJobsResponse } from '../../types';
import CardSkeleton from '../skeletones/CardSkeleton.vue';
import Pagination from '@/components/Pagination.vue';
import JobCard from './JobCard.vue';
import ErrorToast from '../ErrorToast.vue';
import useFetchData from '../../composables/useFetchData';
import { watch } from 'vue';
import { useComputedPage } from '@/composables/useComputed';

const { page } = useComputedPage();

const { data, doRequest, isLoading, error } = useFetchData<GetJobsResponse>(
  () => getJobs(page.value)
);

watch(page, () => {
  doRequest();
});

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
      v-else
      v-for="({ id, title, description, industry }, index) in data?.jobs"
      :key="id"
      v-bind="{ id, title, description, industry }"
      :class="{ elevated: index % 2 != 0 }"
    />
  </div>
  <Pagination
    :key="`${data?.total_jobs}-${page}-${data?.jobs_per_page}`"
    :total_jobs="data?.total_jobs"
    :jobs_per_page="data?.jobs_per_page"
    :page="page"
  />
  <transition name="slide">
    <ErrorToast
      v-if="error"
      :error="error?.message"
      @clear-error="error = null"
    />
  </transition>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';
@import '../../styles/transitions/slide.scss';

.jobs {
  display: flex;
  flex-direction: column;
  align-items: center;

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
