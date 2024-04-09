<script setup lang="ts"></script>

<template>
  <div class="modal">
    <div class="form">
      <h2>You have successfully registered</h2>
      <div class="form__footer">
        <p>Now You may proceed to</p>
        <RouterLink to="/login" class="form__footer-link"> Log In </RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import "../../styles/form.scss";
@import "../../styles/mixins.scss";

.modal {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

h2 {
  font-size: 16px;
  margin: 0;
  text-align: center;

  @include onTablet {
    font-size: 20px;
  }
}
</style>
