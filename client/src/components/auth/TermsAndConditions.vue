<script setup lang="ts">
const emit = defineEmits(["termsAccepted"]);
</script>

<template>
  <div class="terms">
    <input type="checkbox" @change="emit('termsAccepted')" />
    <p>
      I accept the
      <button type="button" class="terms__button">terms and conditions</button>
    </p>
  </div>
</template>

<style scoped lang="scss">
.terms {
  display: flex;
  gap: 7px;

  &__button {
    font-size: 16px;
    color: var(--c-blue);
    background: none;
    border: none;
    cursor: pointer;
  }
}
</style>
