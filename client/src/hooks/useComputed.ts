import type { QueryParams } from '@/types';
import { computed } from 'vue';
import { useRoute } from 'vue-router';

function useComputedPage() {
  const route = useRoute();
  const page = computed(() => {
    const query = route.query as QueryParams<string>;

    return query.page || '1';
  });

  const jobType = computed(() => {
    const query = route.query as QueryParams<string>;

    return query.jobType || '';
  });

  const education = computed(() => {
    const query = route.query as QueryParams<string>;

    return query.education || '';
  });

  const industry = computed(() => {
    const query = route.query as QueryParams<string>;

    return query.industry || '';
  });

  const salary = computed(() => {
    const query = route.query as QueryParams<string>;

    return query.salary;
  });

  return { page, jobType, education, industry, salary };
}

export { useComputedPage };
