import type { GetJobResponse, GetJobsResponse, Job } from "@/types";

const userJobsCache: Record<string, Job[]> = {};

const appliedJobsCache: Record<string, Job[]> = {};

const jobsCache: Record<string, GetJobsResponse> = {};

const jobCache: Record<string, GetJobResponse> = {};

export { userJobsCache, jobsCache, jobCache, appliedJobsCache };
