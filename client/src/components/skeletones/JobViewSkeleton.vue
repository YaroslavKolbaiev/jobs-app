<template>
  <div>
    <div class="job grid__item--1-8">
      <div class="skeleton skeleton__title" />
      <div class="skeleton skeleton__company" />
      <div class="flex-between-center">
        <div class="skeleton applyBtn" />
        <div class="skeleton candidates" />
      </div>
      <div v-for="item in 5" :key="item" class="skeleton skeleton__line" />
      <div v-for="item in 5" :key="item" class="skeleton__short-lines">
        <div class="skeleton skeleton__line skeleton__short-line" />
        <div class="skeleton skeleton__line skeleton__short-line" />
      </div>
    </div>
    <div class="job-details grid__item--9-12">
      <div class="job">
        <div v-for="item in 5" :key="item" class="skeleton skeleton__line" />
      </div>
      <div class="job">
        <div v-for="item in 4" :key="item" class="skeleton skeleton__line" />
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import "../../styles/mixins.scss";
@import "../../styles/job.scss";
@import "../../styles/skeletones.scss";
</style>
