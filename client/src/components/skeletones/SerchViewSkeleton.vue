<template>
  <div class="search-skeleton">
    <div v-for="item in 4" :key="item" v-if="true" class="skeleton__card">
      <div class="skeleton skeleton__title" />

      <div v-for="item in 5" :key="item" class="skeleton skeleton__line" />

      <div class="flex-between-center">
        <div v-for="item in 4" :key="item" class="skeleton skeleton__circle" />
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';
@import '../../styles/skeletones.scss';

.skeleton__card {
  padding: 20px;
  width: 100%;

  @include onDesktop {
    flex-basis: calc(50% - var(--results-gap));
  }
}

.search-skeleton {
  display: flex;
  flex-wrap: wrap;
  gap: var(--results-gap);
}
</style>
