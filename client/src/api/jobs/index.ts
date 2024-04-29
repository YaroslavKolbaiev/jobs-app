import { accessTokenService } from "@/services/accessTokenService";
import type {
  GetJobsResponse,
  GetJobResponse,
  Job,
  PostJobProps,
} from "../../types";
import axios from "axios";
import { jobCache, jobsCache, userJobsCache } from "@/cache";

const BASE_URL = import.meta.env.VITE_API_URL;
const JOB_KEY = "job-";

async function get_jobs(
  page: string = "1",
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

async function get_job(id: string) {
  const key = JOB_KEY + id;
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

async function userJobs() {
  const accessToken = accessTokenService.get();

  if (!accessToken) {
    return;
  }

  if (userJobsCache[accessToken]) {
    return userJobsCache[accessToken];
  }

  const response = await axios.get<Job[]>(`${BASE_URL}/api/jobs-by-user/`, {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
    withCredentials: true,
  });

  const data = response.data;
  userJobsCache[accessToken] = data;

  return data;
}

async function postJob(newJob: PostJobProps) {
  const accessToken = accessTokenService.get();

  if (!accessToken) {
    return;
  }

  try {
    const response = await axios.post<Job>(`${BASE_URL}/api/jobs/new`, newJob, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
      withCredentials: true,
    });

    const data = response.data;
    userJobsCache[accessToken].push(data);

    // Add new job to the cache
    const key = JOB_KEY + data.id;
    jobCache[key] = { job: data, candidates: 0 };

    // Clear the jobs cache
    Object.keys(jobsCache).forEach((key) => {
      delete jobsCache[key];
    });

    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.message);
    }
  }
}

export { get_jobs, get_job, userJobs, postJob };
