<script setup lang="ts">
import { ref, watchEffect, defineEmits } from "vue";
import IconError from "./icons/IconError.vue";

const { error } = defineProps<{ error: string | undefined }>();
const emit = defineEmits(["clear-error"]);

const visible = ref(false);

watchEffect(() => {
  visible.value = true;
  setTimeout(() => {
    visible.value = false;
    emit("clear-error");
  }, 3000);
});
</script>

<template>
  <div v-if="visible" class="toast">
    <div>
      <IconError />
      <span>Oopssss....</span>
    </div>
    <p>{{ error }}</p>
  </div>
</template>

<style scoped lang="scss">
.toast {
  z-index: 10;
  position: fixed;
  min-width: 240px;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #b22222;
  color: white;
  padding: 25px;
  border-radius: 10px;

  & > div {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #421613;
    font-size: 24px;
    font-weight: 600;
  }
}
</style>
