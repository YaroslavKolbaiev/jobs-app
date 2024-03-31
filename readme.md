# Jobs App

<template>
  <div class="skeleton-card">
    <div class="skeleton skeleton__title" />
    <div v-for="item in 5" :key="item" class="skeleton skeleton__line" />
    <div class="skeleton skeleton__short-line" />
    <div class="skeleton skeleton__circle" />
  </div>
</template>

<style scoped lang="scss">
@import '../../styles/mixins.scss';

 <JobMainInfo
          :candidates="data.candidates"
          :title="data.job?.title"
          :address="data.job?.address"
          :company="data.job?.company"
          :description="data.job?.description"
        />
        <JobInfoTable
          :education="data.job?.education"
          :experience="data.job?.experience"
          :salary="data.job?.salary"
          :industry="data.job?.industry"
          :job-type="data.job?.jobType"
        />
      </div>
      <div class="grid__item--9-12">
        <div class="job-details">
          <JobDetails
            :email="data.job?.email"
            :created-at="data.job?.created_at"
            :last-date="data.job?.lastDate"
            class="job"
          />
