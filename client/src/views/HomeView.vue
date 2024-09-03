<script setup lang="ts">
import About from '@/components/Home/About.vue';
import LatestJobs from '@/components/Home/LatestJobs.vue';
import SearchJobs from '@/components/Home/SearchJobs.vue';
</script>

<template>
  <main>
    <div class="container">
      <div class="warning">
        Postgress SQL free tier has expired
        <p>Data is not available.</p>
      </div>
      <div class="grid">
        <About />
        <LatestJobs />
      </div>
    </div>
    <SearchJobs />
  </main>
</template>

<style scoped lang="scss">
.warning {
  color: red;
  text-align: center;
  font-size: 24px;
  :only-child {
    font-size: 20px;
    text-decoration: underline;
  }
}
</style>
