<script setup lang="ts">
import type { InfoTableProps } from '@/types';

const props = defineProps<InfoTableProps>();

const labels = [
  'Job Type',
  'Education',
  'Experiance',
  'Expected Salary',
  'Industry',
];
</script>

<template>
  <h4>Job Summary</h4>
  <table>
    <tr
      v-for="(item, index) in Object.values(props)"
      :key="item"
      :class="{ withBg: index % 2 === 0 }"
    >
      <th>{{ labels[index] }}</th>
      <td>{{ item }}</td>
    </tr>
  </table>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';
h4 {
  margin-bottom: 10px;
  color: var(--c-main-text);
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
  color: var(--c-gray);

  @include onTablet {
    font-size: 16px;
  }
}

th {
  padding: 10px;
  text-align: start;
}

.withBg {
  background-color: var(--row-bg);
}
</style>
