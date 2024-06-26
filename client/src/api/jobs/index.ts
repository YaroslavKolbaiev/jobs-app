import { accessTokenService } from "@/services/accessTokenService";
import type {
  GetJobsResponse,
  GetJobResponse,
  Job,
  PostJobProps,
  ApplyToJobResponse,
} from "../../types";
import axios from "axios";
import { jobCache, jobsCache, userJobsCache, appliedJobsCache } from "@/cache";

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

async function appliedJobs() {
  const accessToken = accessTokenService.get();

  if (!accessToken) {
    return;
  }

  if (appliedJobsCache[accessToken]) {
    return appliedJobsCache[accessToken];
  }

  const response = await axios.get<Job[]>(
    `${BASE_URL}/api/candidate/user-candidate-jobs/`,
    {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
      withCredentials: true,
    }
  );

  const data = response.data;
  appliedJobsCache[accessToken] = data;

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

    // Add new job to the cache
    const key = JOB_KEY + data.id;
    jobCache[key] = { job: data, candidates: 0 };

    // Clear the jobs cache
    Object.keys(jobsCache).forEach((key) => {
      delete jobsCache[key];
    });

    userJobsCache[accessToken].push(data);

    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.message);
    }
  }
}

async function applyToJob(jobId: string) {
  const accessToken = accessTokenService.get();

  if (!accessToken) {
    throw new Error("Login to apply to a job");
  }

  try {
    const response = await axios.post<ApplyToJobResponse>(
      `${BASE_URL}/api/candidate/apply/${jobId}`,
      null,
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
        withCredentials: true,
      }
    );

    const data = response.data;

    const key = JOB_KEY + data.job.id;
    jobCache[key].candidates += 1;

    appliedJobsCache[accessToken].push(data.job);

    return data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.message);
    }
  }
}

async function deleteJob(jobId: string) {
  const accessToken = accessTokenService.get();

  if (!accessToken) {
    return;
  }

  try {
    await axios.delete(`${BASE_URL}/api/jobs/delete/${jobId}`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
      withCredentials: true,
    });

    Object.keys(jobsCache).forEach((key) => {
      delete jobsCache[key];
    });

    const key = JOB_KEY + jobId;
    delete jobCache[key];

    delete userJobsCache[accessToken];
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.message);
    }
  }
}

export {
  get_jobs,
  get_job,
  userJobs,
  postJob,
  applyToJob,
  appliedJobs,
  deleteJob,
};
