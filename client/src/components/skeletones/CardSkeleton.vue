<template>
  <div class="skeleton__card">
    <div class="skeleton skeleton__title" />
    <div v-for="item in 5" :key="item" class="skeleton skeleton__line" />
    <div class="skeleton skeleton__short-line" />
    <div class="skeleton skeleton__circle" />
  </div>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';

.skeleton__card {
  width: 280px;
  padding: 32px;

  @include onTablet {
    width: calc(50% - var(--jobs-gap));
  }
}
</style>
