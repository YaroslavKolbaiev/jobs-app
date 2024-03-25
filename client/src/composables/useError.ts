import { ref } from 'vue';
export default function () {
  const error = ref<Error | null>(null);

  const setError = (value: Error) => {
    error.value = value;
  };

  return {
    error,
    setError,
  };
}
