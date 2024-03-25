<template>
  <div class="card-skeleton">
    <div class="skeleton-header" />
    <div class="skeleton-line" />
    <div class="skeleton-line" />
    <div class="skeleton-line" />
    <div class="skeleton-line" />
    <div class="skeleton-line" />
    <div class="skeleton-short-line" />
    <div class="skeleton-button" />
  </div>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';

.card-skeleton {
  width: 280px;
  box-shadow: 0 9px 18px rgba(37, 41, 49, 0.03);
  border-radius: 16px;
  padding: 32px;
  box-sizing: border-box;
  background-color: var(--card-bg);

  @include onTablet {
    width: calc(50% - var(--jobs-gap));
  }

  & > div {
    background: linear-gradient(
      90deg,
      var(--card-bg) 25%,
      var(--skeleton-line1) 50%,
      var(--skeleton-line2) 75%
    );
    background-size: 200% 100%;
    animation: loading 1.5s infinite;
  }
}

.skeleton-header {
  height: 30px;
  margin-bottom: 20px;
  border-radius: 20px;
}

.skeleton-line {
  height: 10px;
  margin-bottom: 10px;
  border-radius: 10px;
}

.skeleton-short-line {
  height: 10px;
  width: 50%;
  margin-top: 20px;
  margin-bottom: 20px;
  border-radius: 10px;
}

.skeleton-button {
  @include square_32;
  border-radius: 50%;
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
