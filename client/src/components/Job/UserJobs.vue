<script setup lang="ts">
import ListItemSkeleton from "@/components/skeletones/ListItemSkeleton.vue";
import DeleteJob from "@/components/Job/DeleteJob.vue";
import useFetchData from "@/hooks/useFetchData";
import { watch } from "vue";
import type { Job } from "@/types";
import { JobsByUser } from "@/enums";

const { callBack } = defineProps<{
  callBack: () => Promise<Job[] | undefined>;
  usersJobs: JobsByUser;
}>();

const emit = defineEmits(["errorEmited"]);

const { data, isLoading, error, doRequest } = useFetchData(() => callBack());

watch(error, () => {
  emit("errorEmited", error);
});

doRequest();
</script>

<template>
  <div
    :class="`grid__item--${
      usersJobs === JobsByUser.Created ? '6-12' : '7-12'
    } job`"
  >
    <h2>{{ usersJobs }} Jobs</h2>
    <ul>
      <li v-if="!isLoading" v-for="job in data" :key="job.id">
        <RouterLink :to="`/job/${job.id}`" class="link">
          {{ job.title }}
        </RouterLink>
        <DeleteJob
          v-if="usersJobs === JobsByUser.Created"
          :job-id="job.id.toString()"
          @job-deleted="doRequest"
        />
      </li>
      <ListItemSkeleton v-else />
    </ul>
    <p v-if="!data?.length && !isLoading">You don't have any jobs yet</p>
  </div>
</template>

<style scoped lang="scss">
@import "../../styles/gridFlex.scss";
@import "../../styles/job.scss";
@import "../../styles/mixins.scss";

.job {
  margin-bottom: 10px;

  @include onDesktop {
    margin-bottom: 0;
  }
}

h2 {
  color: var(--c-main-text);
}

li {
  line-height: 30px;
  list-style: none;
  position: relative;
  display: flex;

  &::before {
    content: "•";
    position: absolute;
    left: -1em;
    color: var(--c-gray);
  }
}

.link {
  text-decoration: none;
  color: var(--c-gray);
  transition: color 200ms;

  &:hover {
    color: var(--c-blue);
  }
}

p {
  color: var(--c-gray);
}
</style>
