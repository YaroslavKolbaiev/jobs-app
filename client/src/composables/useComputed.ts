import type { GetJobResponse } from '@/types';
import { computed, type Ref } from 'vue';

function useComputed(data: Ref<GetJobResponse | null>) {
  const job = computed(() => data.value?.job);

  const mainInfoProps = computed(() => {
    return {
      title: job.value?.title,
      company: job.value?.company,
      address: job.value?.address,
      candidates: data.value?.candidates,
      description: job.value?.description,
    };
  });

  const jobDetailsProps = computed(() => {
    return {
      email: job.value?.email,
      createdAt: job.value?.created_at,
      lastDate: job.value?.lastDate,
    };
  });

  const jobInfoTableProps = computed(() => {
    return {
      jobType: job.value?.jobType,
      education: job.value?.education,
      experience: job.value?.experience,
      salary: job.value?.salary,
      industry: job.value?.industry,
    };
  });

  const isExpired = computed(() => {
    const isExpired = new Date(job.value?.lastDate as string) > new Date();

    return isExpired;
  });

  return { mainInfoProps, jobDetailsProps, jobInfoTableProps, isExpired };
}

export { useComputed };
