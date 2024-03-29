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
      <div class="search-wrapper">
        <input
          type="text"
          v-model="keyword"
          placeholder="Enter Your keyword"
          required
        />
        <IconSearch />
      </div>
      <div class="search-wrapper">
        <input
          type="text"
          v-model="location"
          placeholder="Enter Your City"
          required
        />
        <IconCity />
      </div>
      <button class="button clickable" type="submit">Search</button>
    </form>
  </div>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';

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

input {
  box-sizing: border-box;
  width: 100%;
  border-radius: 40px;
  padding: 20px 20px 20px 40px;
  background: none;
  border: 1px solid var(--c-blue);
  transition: all 0.3s ease-in-out;
  font-size: 16px;
  color: var(--c-main-text);

  &::placeholder {
    color: var(--c-gray);
    opacity: 0.5;
  }

  &:focus {
    outline: none;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  &:hover {
    border-color: #1f7ace;
  }
}

button {
  border-radius: 40px;
  font-size: 18px;
  font-weight: 600;
  padding: 12px 16px;
}

.search-wrapper {
  position: relative;
}

.placeholder-icon {
  position: absolute;
  top: 50%;
  left: 15px;
  transform: translateY(-50%);
  stroke: var(--c-main-text);
  opacity: 0.5;
}
</style>
