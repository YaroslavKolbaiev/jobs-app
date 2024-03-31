import type { QueryParams } from '@/types';
import { computed } from 'vue';
import { useRoute } from 'vue-router';

function useComputedPage() {
  const route = useRoute();
  const page = computed(() => {
    const query = route.query as QueryParams<string>;

    return query.page || '1';
  });

  return { page };
}

export { useComputedPage };
