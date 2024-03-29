<script setup lang="ts">
const { isExpired } = defineProps<{ isExpired: boolean }>();
</script>

<template>
  <div>
    <div class="job grid__item--1-8">
      <div class="skeleton title" />
      <div class="skeleton company" />
      <div class="flex-between-center">
        <div class="skeleton applyBtn" />
        <div class="skeleton candidates" />
      </div>
      <div v-for="item in 5" :key="item" class="skeleton line" />
      <div v-for="item in 5" :key="item" class="short-lines">
        <div class="skeleton line short" />
        <div class="skeleton line short" />
      </div>
    </div>
    <div class="job-details grid__item--9-12">
      <div class="job">
        <div v-for="item in 5" :key="item" class="skeleton line" />
      </div>
      <div v-if="!isExpired" class="job">
        <div v-for="item in 4" :key="item" class="skeleton line" />
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';

.skeleton {
  border-radius: 20px;
  margin-bottom: 15px;
  background: linear-gradient(
    90deg,
    var(--card-bg) 25%,
    var(--skeleton-line1) 50%,
    var(--skeleton-line2) 75%
  );
  background-size: 200% 100%;
  animation: loading 1.5s infinite;
}

.title {
  height: 35px;
  width: 40%;
}

.company {
  height: 25px;
  width: 100%;
}

.applyBtn {
  height: 40px;
  width: 20%;
}

.candidates {
  height: 25px;
  width: 70%;
}

.line {
  height: 15px;
  width: 100%;
}

.short-lines {
  display: flex;
  gap: 10%;
}

.short {
  width: 30%;
}

@keyframes loading {
  0% {
    background-position: 200% 0;
  }
  100% {
    background-position: -200% 0;
  }
}
</style>
