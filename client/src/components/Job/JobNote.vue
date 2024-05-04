<script setup lang="ts">
const { lastDate } = defineProps<{ lastDate: string }>();

const isExpired = new Date(lastDate) > new Date();
</script>

<template>
  <div v-if="!isExpired" class="job note">
    <h3>Note</h3>
    <p>
      You may not longer apply to this job. This job is expired. Check out other
      jobs on <strong>Ultimate Job</strong>
    </p>
  </div>
</template>

<style scoped lang="scss">
div {
  color: var(--c-main-text);
}
h3 {
  margin: 0;
}

strong {
  color: var(--c-blue);
}

.note {
  background-color: rgba(255, 127, 127, 0.6) !important;
}
</style>
