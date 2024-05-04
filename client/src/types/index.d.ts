interface Job {
  id: string;
  title: string;
  description: string | null;
  email: string;
  address: string | null;
  salary: number | null;
  position: number | null;
  company: string | null;
  // point: {
  //   type: string;
  //   coordinates: [number, number];
  // };
  point: string;
  lastDate: string;
  user: string | null;
  created_at: string;
  jobType: string;
  education: string;
  industry: string;
  experience: string;
}

interface User {
  email: string;
  first_name: string;
  last_name: string;
  resume?: string;
  username: string;
}

interface UserCredentials extends User {
  password: string;
  confirmPassword: string;
}

interface QueryParams<T> {
  [key: string]: T;
}

type GetUserResponse = {
  data: User;
  access_token: string;
};

type GetJobsResponse = {
  jobs: Job[];
  total_jobs: number;
  jobs_per_page: number;
};

type GetJobResponse = {
  job: Job | null;
  candidates: number;
};

type ApplyToJobResponse = {
  appliedAt: string;
  job: Job;
  resume: string;
  user: number;
};

type InfoTableProps = {
  jobType: string | undefined;
  education: string | undefined;
  industry: string | undefined;
  experience: string | undefined;
  salary: number | null | undefined;
};

type MainInfoProps = {
  jobId: string;
  title: string | undefined;
  company: string | null | undefined;
  address: string | null | undefined;
  candidates: number | undefined;
  description: string | null | undefined;
};

type DetailsProps = {
  email: string | undefined;
  created_at: string | undefined;
  lastDate: string | undefined;
};

type CardProps = Pick<Job, "id" | "title" | "description" | "industry">;
type PostJobProps = Pick<
  Job,
  | "title"
  | "description"
  | "email"
  | "address"
  | "salary"
  | "position"
  | "company"
  | "jobType"
  | "industry"
  | "experience"
>;

type NewJobProps = {
  options: unknown;
  name: string;
};

export {
  Job,
  GetJobsResponse,
  CardProps,
  GetJobResponse,
  DetailsProps,
  MainInfoProps,
  InfoTableProps,
  QueryParams,
  GetUserResponse,
  User,
  UserCredentials,
  NewJobProps,
  PostJobProps,
  ApplyToJobResponse,
};
