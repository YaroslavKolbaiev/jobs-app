<script setup lang="ts">
import type { NewJobProps } from "@/types";

const { options, name } = defineProps<NewJobProps>();
const emit = defineEmits(["emitSelect"]);
</script>

<template>
  <select
    @change="(e) => emit('emitSelect', (e.target as HTMLSelectElement)?.value)"
  >
    <option value="" disabled selected>
      Select {{ name }}
    </option>

    <option v-for="type in options" :key="type" :value="type">
      {{ type }}
    </option>
  </select>
</template>
