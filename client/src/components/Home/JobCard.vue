<script setup lang="ts">
import { defineProps } from 'vue';
import ArrowRight from '../icons/IconArrowRight.vue';
import type { CardProps } from '../../types';
import { slicer } from '@/utils';

const { id, title, description, industry } = defineProps<CardProps>();
</script>
<template>
  <div class="jobCard">
    <h4 class="jobCard__title">
      {{ title }}
    </h4>
    <p class="jobCard__description">
      {{ description ? slicer(180, description) : 'No description' }}
    </p>
    <p class="jobCard__industry">
      {{ industry }}
    </p>
    <RouterLink :to="`/job/${id}`" class="jobCard__learn-more">
      <ArrowRight class="jobCard__arrow" />
      <span>Learn more</span>
    </RouterLink>
  </div>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';

.jobCard {
  width: 280px;
  box-shadow: 0 9px 18px rgba(37, 41, 49, 0.03);
  background-color: var(--card-bg);
  border-radius: 16px;
  padding: 32px;
  box-sizing: border-box;

  @include onTablet {
    width: calc(50% - var(--jobs-gap));
  }

  &__title {
    width: fit-content;
    border-radius: 23px;
    font-size: 13px;
    line-height: 20px;
    text-transform: uppercase;
    color: var(--c-blue);
    margin: 0 0 20px;
    padding: 5px 10px;
    background-color: var(--main-bg);
  }

  &__description {
    font-size: 13px;
    line-height: 150%;
    margin: 0 0 10px;
    color: var(--c-gray);
  }

  &__industry {
    margin: 0 0 10px;
    color: var(--c-main-text);
  }

  &__learn-more {
    width: fit-content;
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
    font-size: 15px;
    color: var(--c-main-text);
  }

  &__arrow {
    border-radius: 50%;
    padding: 3px;
    @include square_32;
    background-color: var(--c-blue);
    transition: all 600ms;

    &:hover {
      transform: rotate(360deg);
    }
  }
}
</style>
