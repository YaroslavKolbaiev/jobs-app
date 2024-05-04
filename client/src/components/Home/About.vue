<template>
  <div class="about grid__item--1-4">
    <h3 class="about__title">
      <span class="about__highlight">Ultimate Job </span>is a full service job
      searching platform
    </h3>

    <p class="about__paragraph">
      Deep analytics, strong strategy and bright creative ideas.
    </p>

    <p class="about__paragraph">
      We are sure that first-rate job is possible only if all three components
      are united.
    </p>
  </div>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';
.about {
  width: 100%;
  margin-bottom: 40px;

  @include onTablet {
    width: 290px;
  }
  &__title {
    font-size: 20px;
    line-height: 150%;
    margin: 0 0 24px;
    color: var(--c-main-text);
  }

  &__paragraph {
    margin: 0 0 21px;
    font-weight: 400;
    font-size: 14px;
    line-height: 130%;
    color: #6c788b;

    &:last-child {
      margin-bottom: 0;
    }
  }

  &__highlight {
    color: var(--c-blue);
  }
}
</style>
