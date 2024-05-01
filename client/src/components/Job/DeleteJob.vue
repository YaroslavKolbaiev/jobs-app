<script setup lang="ts">
import { deleteJob } from "@/api/jobs";
import ErrorToast from "@/components/ErrorToast.vue";
import IconDelete from "@/components/icons/IconDelete.vue";
import useFetchData from "@/hooks/useFetchData";

const { jobId } = defineProps<{ jobId: string }>();

const emit = defineEmits(["job-deleted"]);

const onJobDeleted = async () => {
  await deleteJob(jobId);
  emit("job-deleted");
};

const { isLoading, error, doRequest } = useFetchData(onJobDeleted);
</script>

<template>
  <button type="button" @click="doRequest" :disabled="isLoading">
    <IconDelete />
  </button>

  <transition name="slide">
    <ErrorToast
      v-if="error"
      :error="error?.message"
      @clear-error="error = null"
    />
  </transition>
</template>

<style scoped lang="scss">
@import "../../styles/transitions/slide.scss";

button {
  margin-left: 10px;
  background: none;
  border: none;
  cursor: pointer;
  fill: var(--c-main-text);

  &:disabled {
    opacity: 0.5;
  }
}
</style>
