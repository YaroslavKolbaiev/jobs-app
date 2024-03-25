import { ref, onMounted, type UnwrapRef } from 'vue';
import useError from './useError';
import useIsLoading from './useIsLoading';
import { wait } from '@/utils';

export default function useFetchData<T>(handler: () => Promise<T>) {
  const { error, setError } = useError();
  const { isLoading, setIsLoading } = useIsLoading();

  const data = ref<T | null>(null);

  const doRequest = () => {
    onMounted(async () => {
      setIsLoading(true);
      try {
        await wait(4000);
        data.value = (await handler()) as UnwrapRef<T>;
      } catch (err) {
        if (err instanceof Error) {
          setError(err);
        }
      } finally {
        setIsLoading(false);
      }
    });
  };

  return { doRequest, error, isLoading, data };
}
