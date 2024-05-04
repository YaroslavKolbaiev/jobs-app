<template>
  <div
    v-for="item in 4"
    :key="`${item}-id`"
    class="skeleton skeleton__short-line"
  />
</template>

<style scoped lang="scss">
@import "../../styles/mixins.scss";
@import "../../styles/skeletones.scss";
</style>
