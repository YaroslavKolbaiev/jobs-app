<script setup lang="ts">
import IconEye from '@/components/icons/IconEye.vue';
import IconEyeX from '@/components/icons/IconEyeX.vue';

const { show } = defineProps<{ show: boolean }>();
</script>

<template>
  <button class="show-password form__icon form__icon--password" type="button">
    <IconEye v-if="show" />
    <IconEyeX v-else />
  </button>
</template>

<style scoped lang="scss">
.show-password {
  border: none;
  background: none;
  padding: 0;
  display: flex;
  cursor: pointer;
}
</style>
