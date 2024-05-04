import type { filters } from '@/enums';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

function useFilter() {
  const router = useRouter();
  const filterButton = ref<keyof typeof filters>('hidden');

  const toggleFilter = (e: Event) => {
    filterButton.value = (e.currentTarget as HTMLButtonElement)
      ?.name as keyof typeof filters;
  };

  const onFilterChange = (e: Event) => {
    const target = e.target as HTMLInputElement;
    const query = router.currentRoute.value.query as Record<string, string>;

    if (target.checked) {
      router.push({
        query: { ...query, [filterButton.value]: target.value },
      });
      filterButton.value = 'hidden';
    } else {
      delete query[filterButton.value];
      router.push({ query });
    }
  };

  const clearFilters = () => {
    router.push({ query: {} });
  };

  return { filterButton, toggleFilter, onFilterChange, clearFilters };
}

export { useFilter };
