<template>
  <svg class="loader" viewBox="0 0 800 800" xmlns="http://www.w3.org/2000/svg">
    <circle
      class="spin2"
      cx="400"
      cy="400"
      fill="none"
      r="200"
      stroke-width="40"
      stroke="#ffffff"
      stroke-dasharray="700 1400"
      stroke-linecap="round"
    />
  </svg>
</template>

<style scoped>
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes spin2 {
  0% {
    stroke-dasharray: 1, 800;
    stroke-dashoffset: 0;
  }
  50% {
    stroke-dasharray: 400, 400;
    stroke-dashoffset: -200px;
  }
  100% {
    stroke-dasharray: 800, 1;
    stroke-dashoffset: -800px;
  }
}

.spin2 {
  transform-origin: center;
  animation: spin2 1.5s ease-in-out infinite, spin 2s linear infinite;
  animation-direction: alternate;
}

.loader {
  height: var(--auth-btn-height);
}
</style>
