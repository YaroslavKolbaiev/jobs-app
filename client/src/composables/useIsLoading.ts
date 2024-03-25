import { ref } from 'vue';
export default function () {
  const isLoading = ref(false);

  const setIsLoading = (value: boolean) => {
    isLoading.value = value;
  };

  return {
    isLoading,
    setIsLoading,
  };
}
