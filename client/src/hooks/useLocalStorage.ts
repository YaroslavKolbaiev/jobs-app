import { ref, watch } from 'vue';

export function useLocalStorage(key: string, initialValue: boolean) {
  const storedValue = localStorage.getItem(key);
  const initial = storedValue ? JSON.parse(storedValue) : initialValue;
  const data = ref(initial);

  watch(data, (newVal) => {
    localStorage.setItem(key, JSON.stringify(newVal));
  });

  const setLocalStorage = (value: boolean) => {
    data.value = value;
  };

  return { data, setLocalStorage };
}
