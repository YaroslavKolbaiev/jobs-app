<script setup lang="ts">
import ArrowRight from './icons/IconArrowRight.vue';
const data = [
  {
    title: 'Job1 Updated',
    description:
      'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available',
    email: 'test@gmail.com',
    address: 'test address',
    salary: 10000,
    position: 1,
    company: 'test company',
    point: 'POINT(0.0 0.0)',
    lastDate: '2024-03-28T04:30:50.992728Z',
    user: '1',
    created_at: '2024-03-20T04:30:50.992728Z',
    jobType: 'Permanent',
    education: 'Bachelor',
    industry: 'IT',
    experience: 'No Experience',
  },
  {
    title: 'Job2 Updated',
    description:
      'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available',
    email: 'test2@gmail.com',
    address: 'test address2',
    salary: 20000,
    position: 2,
    company: 'test company2',
    point: 'POINT(0.0 0.0)',
    lastDate: '2024-03-28T04:30:50.992728Z',
    user: '1',
    created_at: '2024-03-20T04:30:50.992728Z',
    jobType: 'Permanent',
    education: 'Bachelor',
    industry: 'IT',
    experience: 'No Experience',
  },
  {
    title: 'Job3 Updated',
    description:
      'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available',
    email: 'test3@gmail.com',
    address: 'test address3',
    salary: 30000,
    position: 2,
    company: 'test company3',
    point: 'POINT(0.0 0.0)',
    lastDate: '2024-03-28T04:30:50.992728Z',
    user: '1',
    created_at: '2024-03-20T04:30:50.992728Z',
    jobType: 'Permanent',
    education: 'Bachelor',
    industry: 'IT',
    experience: 'No Experience',
  },
  {
    title: 'Job3 Updated',
    description:
      'In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available',
    email: 'test3@gmail.com',
    address: 'test address3',
    salary: 30000,
    position: 2,
    company: 'test company3',
    point: 'POINT(0.0 0.0)',
    lastDate: '2024-03-28T04:30:50.992728Z',
    user: '1',
    created_at: '2024-03-20T04:30:50.992728Z',
    jobType: 'Permanent',
    education: 'Bachelor',
    industry: 'Telecommunication',
    experience: 'No Experience',
  },
];
</script>

<template>
  <div class="latest_jobs grid__item--5-12">
    <div
      v-for="(job, index) in data"
      :key="job.title"
      :class="{ elevated: index % 2 != 0 }"
      class="card"
    >
      <h4 class="title">
        {{ job.title }}
      </h4>
      <p class="description">{{ job.description.slice(0, 80) }}...</p>
      <p class="industry">
        {{ job.industry }}
      </p>
      <RouterLink :to="'#'" class="learn-more">
        <ArrowRight class="arrow" />
        <span>Learn more</span>
      </RouterLink>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import '../styles/mixins.scss';

.latest_jobs {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: Poppins, sans-serif;
  gap: var(--jobs-gap);

  @include onTablet {
    flex-direction: row;
    flex-wrap: wrap;
  }
}

.card {
  width: 280px;
  box-shadow: 0 9px 18px rgba(37, 41, 49, 0.03);
  background-color: var(--card-bg);
  border-radius: 16px;
  padding: 32px;
  box-sizing: border-box;

  @include onTablet {
    width: calc(50% - var(--jobs-gap));
  }
}

.title {
  width: fit-content;
  border-radius: 23px;
  font-size: 13px;
  line-height: 20px;
  text-transform: uppercase;
  color: var(--c-blue);
  margin: 0 0 20px;
  padding: 5px;
  background-color: var(--main-bg);
}

.description {
  font-size: 13px;
  line-height: 150%;
  margin: 0 0 10px;
  color: var(--c-gray);
}

.industry {
  margin: 0 0 10px;
  color: var(--c-main-text);
}

.learn-more {
  width: fit-content;
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  font-size: 15px;
  color: var(--c-main-text);
}

.arrow {
  border-radius: 50%;
  padding: 3px;
  @include square_32;
  background-color: var(--c-blue);
  transition: all 600ms;

  &:hover {
    transform: rotate(360deg);
  }
}

.elevated {
  @include onTablet {
    transform: translateY(-50%);
  }
  @include onDesktop {
    transform: translateY(-20%);
  }
}
</style>
