<script setup lang="ts">
import JobMainInfo from "@/components/Job/JobMainInfo.vue";
import ErrorToast from "@/components/ErrorToast.vue";
import JobDetails from "@/components/Job/JobDetails.vue";
import JobInfoTable from "@/components/Job/JobInfoTable.vue";
import JobNote from "@/components/Job/JobNote.vue";
import Map from "@/components/Map.vue";
import JobViewSkeleton from "@/components/skeletones/JobViewSkeleton.vue";
import { useRoute } from "vue-router";
import { get_job } from "@/api/jobs";
import useFetchData from "@/hooks/useFetchData";
import type { GetJobResponse } from "@/types";

const route = useRoute();
const jobId = route.params.id as string;

const { data, doRequest, isLoading, error } = useFetchData<GetJobResponse>(() =>
  get_job(jobId)
);

doRequest();
</script>
<template>
  <main>
    <JobViewSkeleton v-if="isLoading" class="container grid" />
    <div v-if="!isLoading" class="container grid">
      <div class="job grid__item--1-8">
        <JobMainInfo
          :title="data?.job?.title"
          :address="data?.job?.address"
          :description="data?.job?.description"
          :candidates="data?.candidates"
          :company="data?.job?.company"
        />
        <JobInfoTable
          :job-type="data?.job?.jobType"
          :education="data?.job?.education"
          :experience="data?.job?.experience"
          :salary="data?.job?.salary"
          :industry="data?.job?.industry"
        />
      </div>
      <div class="grid__item--9-12">
        <div class="job-details">
          <JobDetails
            :email="data?.job?.email"
            :created_at="data?.job?.created_at"
            :last-date="data?.job?.lastDate"
            class="job"
          />
          <JobNote :last-date="data?.job?.lastDate || ''" />
        </div>
        <Map :point="data?.job?.point" />
      </div>
    </div>
  </main>
  <transition name="slide">
    <ErrorToast
      v-if="error"
      :error="error?.message"
      @clear-error="error = null"
    />
  </transition>
</template>

<style scoped lang="scss">
@import "../styles/transitions/slide.scss";
@import "../styles/job.scss";
</style>
