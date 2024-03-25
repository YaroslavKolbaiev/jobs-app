import type { GetJobsResponse, GetJobResponse } from '../types';
import axios from 'axios';

const BASE_URL = 'http://localhost:8000';
const jobsCache: Record<string, GetJobsResponse> = {};
const jobCache: Record<string, GetJobResponse> = {};

async function getJobs(page: string = '1') {
  const key = 'page-' + page;
  if (jobsCache[key]) {
    return jobsCache[key];
  }

  const response = await axios.get<GetJobsResponse>(
    `${BASE_URL}/api/jobs/?page=${page}`
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
