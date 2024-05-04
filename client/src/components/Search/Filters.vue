<script setup lang="ts">
import IconJobType from '@/components/icons/IconJobType.vue';
import IconEducation from '@/components/icons/IconEducation.vue';
import IconIndustry from '@/components/icons/IconIndustry.vue';
import IconSalary from '@/components/icons/IconSalary.vue';
import { useClickOutside } from '@/hooks/useClickOutside';
import { useFilter } from '@/hooks/useFilter';
import { FilterNames, filters } from '@/enums';
import { useRoute } from 'vue-router';

const route = useRoute();

const { filterButton, toggleFilter, onFilterChange, clearFilters } =
  useFilter();

const nodeRef = useClickOutside(() => (filterButton.value = 'hidden'));
</script>

<template>
  <div class="filters">
    <button type="button" :name="FilterNames.JobType" @click="toggleFilter">
      <IconJobType class="icon" />
    </button>

    <button type="button" :name="FilterNames.Education" @click="toggleFilter">
      <IconEducation class="icon" />
    </button>

    <button type="button" :name="FilterNames.Industry" @click="toggleFilter">
      <IconIndustry class="icon" />
    </button>

    <button type="button" :name="FilterNames.SalaryRange" @click="toggleFilter">
      <IconSalary class="icon" />
    </button>

    <button type="button" class="clear-filters" @click="clearFilters">
      Clear Filters
    </button>

    <Transition name="fade">
      <div ref="nodeRef" v-if="filters[filterButton]" class="window">
        <div v-for="item in filters[filterButton]" :key="item">
          <input
            @change="onFilterChange"
            type="radio"
            :id="item"
            :value="item"
            :name="filterButton"
            :checked="route.query[filterButton] === item"
          />
          <label :for="item">{{ item }}</label>
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped lang="scss">
@import '../../styles/transitions/fade.scss';
@import '../../styles/mixins.scss';

.filters {
  margin-top: 20px;
  display: flex;
  gap: 10px;
  position: relative;
}

.window {
  position: absolute;
  z-index: 10;
  background-color: var(--card-bg);
  border: 1px solid var(--c-gray);
  top: 105%;
  width: max-content;
  padding: 10px 30px 10px 5px;
  box-sizing: border-box;
  border-radius: 10px;
}

button {
  border: 1px solid var(--c-gray);
  background-color: var(--card-bg);
  padding: 3px 5px;
  border-radius: 10px;
  cursor: pointer;

  @include onTablet {
    padding: 5px 10px;
  }
}

input {
  margin-right: 10px;
}

label {
  line-height: 32px;
  color: var(--c-main-text);
  &:hover {
    color: var(--c-blue);
  }
}

.icon {
  fill: var(--c-main-text);
}

.clear-filters {
  font-family: Poppins, sans-serif;
  margin-left: auto;
  color: var(--c-main-text);
}
</style>
