<script setup lang="ts">
import IconSearch from '@/components/icons/IconSearch.vue';
import IconCity from '@/components/icons/IconCity.vue';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const keyword = ref('');
const location = ref('');
const router = useRouter();

const submitForm = () => {
  router.push({
    name: 'search',
    query: { keyword: keyword.value, location: location.value },
  });
};
</script>

<template>
  <div class="search">
    <h2>Search</h2>
    <form @submit.prevent="submitForm">
      <div class="form__wrapper">
        <input
          class="form__input"
          type="text"
          v-model="keyword"
          placeholder="Enter Your keyword"
          required
        />
        <IconSearch />
      </div>
      <div class="form__wrapper">
        <input
          class="form__input"
          type="text"
          v-model="location"
          placeholder="Enter Your City"
        />
        <IconCity />
      </div>
      <button class="button button--form clickable" type="submit">
        Search
      </button>
    </form>
  </div>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';
@import '../../styles/form.scss';
@import '../../styles/buttons.scss';

.search {
  margin-top: 40px;
  background-color: var(--search-bg);
  box-sizing: border-box;

  padding: 10px 20px;

  @include onTablet {
    padding: 20px 40px;
  }
}

h2 {
  color: var(--c-main-text);
  text-align: center;
  margin: 0 0 20px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 420px;
  margin: auto;
}
</style>
