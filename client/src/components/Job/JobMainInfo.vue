<script setup lang="ts">
import type { MainInfoProps } from '@/types';

const { title, company, address, candidates, description } =
  defineProps<MainInfoProps>();
</script>

<template>
  <h1 class="title">
    {{ title }}
  </h1>

  <div class="wrapper">
    <h2 class="name">
      {{ company }}
    </h2>
    <p class="adress">
      {{ address }}
    </p>
  </div>

  <div class="wrapper">
    <button class="button clickable" type="button">Apply Now</button>
    <span class="candidates"
      >{{ candidates }} Candidates have applied for this job</span
    >
  </div>

  <p class="description">
    <strong>Description:</strong>
    <br />
    {{ description }}
  </p>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';

.title {
  color: var(--c-main-text);
  margin: 0;
}

.wrapper {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 20px;

  @include onTablet {
    flex-direction: row;
    align-items: center;
  }
}

.name {
  margin: 0;
  color: var(--c-blue);
}

.adress {
  margin: 0;
  color: var(--c-gray);
}

.candidates {
  color: #228b22;
}

.description {
  margin: 0;
  font-size: 14px;
  color: var(--c-main-text);

  & > strong {
    font-size: 20px;
  }
}
</style>
