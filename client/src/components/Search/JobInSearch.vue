<script setup lang="ts">
import { slicer } from '@/utils';
import IconJobType from '@/components/icons/IconJobType.vue';
import IconEducation from '@/components/icons/IconEducation.vue';
import IconIndustry from '@/components/icons/IconIndustry.vue';
import IconSalary from '@/components/icons/IconSalary.vue';
import IconsLayout from '@/layouts/IconsLayout.vue';
import type { Job } from '@/types';
import { RouterLink } from 'vue-router';

const { jobs } = defineProps<{ jobs: Job[] | undefined }>();
</script>

<template>
  <div class="results">
    <RouterLink
      :to="`/job/${job.id}`"
      v-for="(job, index) in jobs"
      :key="index"
      class="results__box"
    >
      <div class="results__text">
        <h1>{{ job.title }}</h1>
        <p>{{ slicer(320, job.description) }}</p>
      </div>

      <div class="results__icons">
        <IconsLayout :name="job.jobType">
          <IconJobType />
        </IconsLayout>

        <IconsLayout :name="job.education">
          <IconEducation />
        </IconsLayout>

        <IconsLayout :name="job.industry">
          <IconIndustry />
        </IconsLayout>

        <IconsLayout :name="job.salary">
          <IconSalary />
        </IconsLayout>
      </div>
    </RouterLink>
  </div>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';

h1 {
  margin: 0 0 10px;
  font-size: 18px;

  @include onTablet {
    font-size: 24px;
  }
}

p {
  font-size: 12px;
  margin: 0;

  @include onTablet {
    font-size: 16px;
  }
}

.results {
  display: flex;
  flex-wrap: wrap;
  margin-top: 20px;
  gap: var(--results-gap);

  @include onDesktop {
    flex-wrap: nowrap;
    justify-content: space-between;
  }

  &__box {
    display: flex;
    flex-direction: column;
    cursor: pointer;
    transition: transform 200ms;
    text-decoration: none;
    color: var(--c-main-text);

    @include onDesktop {
      flex-basis: calc(50% - var(--results-gap));
    }

    &:hover {
      transform: scale(1.05);
    }

    &:active {
      opacity: 0.6;
    }
  }

  &__text {
    box-shadow: 0 9px 18px rgba(37, 41, 49, 0.03);
    background-color: var(--card-bg);
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
    padding: 20px 20px;
    flex-grow: 1;
  }

  &__icons {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    border-bottom-left-radius: 16px;
    border-bottom-right-radius: 16px;
    color: var(--c-main-text);
    background-color: var(--c-gray);
    padding: 10px 20px;
  }
}
</style>
