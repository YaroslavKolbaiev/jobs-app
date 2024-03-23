<script setup lang="ts">
import About from '../components/About.vue';
import LatestJobs from '../components/LatestJobs.vue';
</script>

<template>
  <main>
    <div class="container">
      <RouterLink :to="'#'" class="search"> Go to Search </RouterLink>
      <div class="grid">
        <About />
        <LatestJobs />
      </div>
    </div>
  </main>
</template>

<style scoped lang="scss">
@import '../styles/mixins.scss';

.search {
  text-decoration: none;
  font-family: Roboto, sans-serif;
  font-size: 18px;
  color: var(--c-blue);

  @include onTablet {
    font-size: 24px;
  }

  &:hover {
    text-decoration: underline;
  }
}
</style>
