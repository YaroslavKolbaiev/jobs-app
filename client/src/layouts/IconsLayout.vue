<script setup lang="ts">
const { name } = defineProps<{ name: string | number }>();
</script>

<template>
  <div>
    <slot></slot>
    <span>{{ name }}</span>
  </div>
</template>

<style scoped lang="scss">
div {
  display: flex;
  gap: 5px;
}
</style>
