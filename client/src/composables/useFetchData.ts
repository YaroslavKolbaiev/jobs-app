import { ref, type UnwrapRef } from 'vue';
import { wait } from '@/utils';

export default function useFetchData<T>(handler: () => Promise<T>) {
  const error = ref<Error | null>(null);
  const isLoading = ref(false);

  const data = ref<T | null>(null);

  const doRequest = async () => {
    isLoading.value = true;
    try {
      await wait(3000);
      data.value = (await handler()) as UnwrapRef<T>;
    } catch (err) {
      if (err instanceof Error) {
        error.value = err;
      }
    } finally {
      isLoading.value = false;
    }
  };

  return {
    doRequest,
    error,
    isLoading,
    data,
  };
}
