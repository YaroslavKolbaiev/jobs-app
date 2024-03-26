interface Job {
  id: string;
  title: string;
  description: string | null;
  email: string;
  address: string | null;
  salary: number;
  position: number;
  company: string | null;
  point: {
    type: string;
    coordinates: [number, number];
  };
  lastDate: string;
  user: string | null;
  created_at: string;
  jobType: string;
  education: string;
  industry: string;
  experience: string;
}

type GetJobsResponse = {
  jobs: Job[];
  total_jobs: number;
  jobs_per_page: number;
};

type GetJobResponse = {
  job: Job;
  candidates: number;
};
type InfoTableProps = {
  jobType: string | undefined;
  education: string | undefined;
  industry: string | undefined;
  experience: string | undefined;
  salary: number | undefined;
};

type MainInfoProps = {
  title: string | undefined;
  company: string | null | undefined;
  address: string | null | undefined;
  candidates: number | undefined;
  description: string | null | undefined;
};

type DetailsProps = {
  email: string | undefined;
  createdAt: string | undefined;
  lastDate: string | undefined;
};

type CardProps = Pick<Job, 'id' | 'title' | 'description' | 'industry'>;

export {
  Job,
  GetJobsResponse,
  CardProps,
  GetJobResponse,
  DetailsProps,
  MainInfoProps,
  InfoTableProps,
};
