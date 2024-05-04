<script setup lang="ts">
import { getVisiblePages } from '@/services/paginationService';

interface Props {
  total_jobs: number | undefined;
  jobs_per_page: number | undefined;
  page: string;
}

const props = defineProps<Props>();

const totalPages = () => {
  if (!props.total_jobs || !props.jobs_per_page) {
    return 0;
  }

  return Math.ceil(props.total_jobs / props.jobs_per_page);
};

const nextPage = String(Number(props.page) + 1);
const prevPage = String(Number(props.page) - 1);

const visiblePages = getVisiblePages(+props.page, totalPages());

const isPagination = totalPages() > 1;
</script>

<template>
  <div v-if="isPagination" class="pagination grid__item--1-12">
    <span class="pagination__page">
      <RouterLink
        class="pagination__link"
        :to="{ path: '.', query: { page: prevPage } }"
      >
        Previous
      </RouterLink>
    </span>
    <span
      v-for="pg in visiblePages"
      :key="pg"
      class="pagination__page pagination__page--numbers"
      :class="{ active: pg === +props.page }"
    >
      <RouterLink
        class="pagination__link"
        :to="{ path: '.', query: { page: pg } }"
      >
        {{ pg }}
      </RouterLink>
    </span>
    <span class="pagination__page">
      <RouterLink
        class="pagination__link"
        :to="{ path: '.', query: { page: nextPage } }"
      >
        Next
      </RouterLink>
    </span>
  </div>
</template>

<style scoped lang="scss">
@import '../styles/mixins.scss';

.pagination {
  margin-top: 40px;
  display: flex;
  justify-content: center;

  &__page {
    width: 100px;
    height: 40px;
    display: flex;
    border: 2px solid var(--c-gray);
    box-sizing: border-box;
    cursor: pointer;
    transition: background 200ms;

    &--numbers {
      width: 60px;
      display: none;

      @include onTablet {
        display: flex;
      }
    }

    &:hover {
      background-color: var(--card-bg);
    }

    &:first-child {
      border-top-left-radius: 5px;
      border-bottom-left-radius: 5px;
    }

    &:last-child {
      border-top-right-radius: 5px;
      border-bottom-right-radius: 5px;
      // border-right: 1px solid var(--c-gray);
    }

    &:not(:last-child) {
      border-right: none;
    }
  }

  &__link {
    text-decoration: none;
    color: var(--c-main-text);
    width: 100%;
    text-align: center;
    line-height: 40px;
  }
}

.active {
  border: 3px solid var(--c-dark-blue);

  &:not(:last-child) {
    border-right: 3px solid var(--c-dark-blue);
  }

  a {
    color: var(--c-blue);
  }

  + .pagination__page {
    border-left: none;
  }
}
</style>
