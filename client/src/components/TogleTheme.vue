<script setup lang="ts">
import IconSun from './icons/IconSun.vue';
import IconMoon from './icons/IconMoon.vue';
import { ref } from 'vue';
const isDark = ref(false);

const toggleTheme = () => {
  document.body.classList.toggle('dark', isDark.value);
};
</script>

<template>
  <figure class="flex-center">
    <IconSun v-if="!isDark" />
    <IconMoon v-if="isDark" />
  </figure>
  <label class="switch" for="checkbox" @change="toggleTheme">
    <input type="checkbox" v-model="isDark" id="checkbox" />
    <span class="slider round" />
  </label>
</template>

<style scoped lang="scss">
@import '../styles/mixins.scss';

figure {
  margin: 0;
  @include square_32;

  @include onTablet {
    @include square_48;
  }
}

.switch {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 20px;

  @include onTablet {
    width: 60px;
    height: 34px;
  }
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: var(--c-gray);
  transition: 0.4s;
}

.slider:before {
  position: absolute;
  content: '';
  height: 16px;
  width: 16px;
  left: 2px;
  bottom: 2px;
  background-color: var(--main-bg);
  transition: 0.4s;

  @include onTablet {
    height: 26px;
    width: 26px;
    left: 4px;
    bottom: 4px;
  }
}

input:checked + .slider {
  background-color: var(--c-blue);
}

input:checked + .slider:before {
  transform: translateX(26px);
}

.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>
