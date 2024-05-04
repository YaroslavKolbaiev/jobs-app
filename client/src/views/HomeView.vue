<script setup lang="ts">
import About from '@/components/Home/About.vue';
import LatestJobs from '@/components/Home/LatestJobs.vue';
import SearchJobs from '@/components/Home/SearchJobs.vue';
</script>

<template>
  <main>
    <div class="container">
      <div class="grid">
        <About />
        <LatestJobs />
      </div>
    </div>
    <SearchJobs />
  </main>
</template>

<style scoped lang="scss"></style>
