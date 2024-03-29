<script setup lang="ts">
import type { DetailsProps } from '@/types';
import dayjs from 'dayjs';
import { computed } from 'vue';

const props = defineProps<DetailsProps>();

const formattedCreatedAt = computed(() =>
  dayjs(props.createdAt).format('DD-MM-YYYY')
);
const formattedLastDate = computed(() =>
  dayjs(props.lastDate).format('DD-MM-YYYY')
);
</script>

<template>
  <div>
    <h3 class="details__title">More Details</h3>

    <hr />

    <div class="details">
      <p>Email Adress</p>
      <span>{{ props.email }}</span>
    </div>

    <div class="details">
      <p>Job Posted</p>
      <span>{{ formattedCreatedAt }}</span>
    </div>

    <div>
      <p>Last Date</p>
      <span>{{ formattedLastDate }}</span>
    </div>
  </div>
</template>

<style scoped lang="scss">
.details {
  margin-bottom: 15px;

  &__title {
    margin: 0;
    color: var(--c-main-text);
  }
}

hr {
  border: 0;
  border-top: 1px solid var(--c-gray);
  margin: 10px 0;
}

p {
  margin: 0;
  color: var(--c-gray);
}

span {
  font-size: 14px;
  color: var(--c-main-text);
}
</style>
