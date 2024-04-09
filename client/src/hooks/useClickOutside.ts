import { ref, watch } from 'vue';

export function useClickOutside(handler: () => void) {
  const domNode = ref<HTMLElement | null>(null);

  watch(domNode, () => {
    const isHandler = (event: MouseEvent) => {
      if (!domNode.value?.contains(event.target as Node)) {
        handler();
      }
    };

    document.addEventListener('mousedown', isHandler);

    return () => {
      document.removeEventListener('mousedown', isHandler);
    };
  });

  return domNode;
}
