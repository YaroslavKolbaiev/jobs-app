import type { GetJobsResponse, GetJobResponse } from '../../types';
import axios from 'axios';

const BASE_URL = import.meta.env.VITE_API_URL;

const jobsCache: Record<string, GetJobsResponse> = {};
const jobCache: Record<string, GetJobResponse> = {};

async function getJobs(
  page: string = '1',
  query: Record<string, string | number> = {}
) {
  const key = `${page}-${JSON.stringify(query)}`;
  if (jobsCache[key]) {
    return jobsCache[key];
  }

  const queryString = new URLSearchParams({ page, ...query }).toString();

  const response = await axios.get<GetJobsResponse>(
    `${BASE_URL}/api/jobs/?${queryString}`
  );

  const data = response.data;
  jobsCache[key] = data;

  return data;
}

async function getJob(id: string) {
  const key = 'job-' + id;
  if (jobCache[key]) {
    return jobCache[key];
  }

  const response = await axios.get<GetJobResponse>(
    `${BASE_URL}/api/jobs/${id}`
  );

  const data = response.data;
  jobCache[key] = data;

  return data;
}

export { getJobs, getJob };
