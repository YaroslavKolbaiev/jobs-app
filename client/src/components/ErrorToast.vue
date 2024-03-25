<script setup lang="ts">
import { ref, watchEffect } from 'vue';
import IconError from './icons/IconError.vue';

const { error } = defineProps<{ error: string | undefined }>();

const visible = ref(false);

watchEffect(() => {
  if (error) {
    visible.value = true;
    setTimeout(() => {
      visible.value = false;
    }, 2000);
  }
});
</script>

<template>
  <transition name="slide">
    <div v-if="visible" class="error-toast">
      <div>
        <IconError />
        <span>Oopssss....</span>
      </div>
      <p>{{ error }}</p>
    </div>
  </transition>
</template>

<style scoped lang="scss">
.error-toast {
  position: fixed;
  min-width: 240px;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #b22222;
  color: white;
  padding: 25px;
  border-radius: 10px;
  font-family: Poppins, sans-serif;

  & > div {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #421613;
    font-size: 24px;
    font-weight: 600;
  }
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.5s;
}

.slide-enter-from {
  transform: translate(-50%, calc(100% + 20px));
}

.slide-enter-to,
.slide-leave-from {
  transform: translate(-50%, 0);
}

.slide-leave-to {
  transform: translate(-50%, calc(100% + 20px));
}
</style>
