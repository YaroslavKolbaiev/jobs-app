export enum FilterNames {
  JobType = "jobType",
  Education = "education",
  Industry = "industry",
  SalaryRange = "salary",
}

export enum JobType {
  Permanent = "Permanent",
  Contract = "Contract",
  Internship = "Internship",
  Temporary = "Temporary",
}

export enum Education {
  Bachelor = "Bachelor",
  Master = "Master",
  PhD = "PhD",
}

export enum Industry {
  IT = "IT",
  Business = "Business",
  Banking = "Banking",
  Education = "Education",
  Telecommunication = "Telecommunication",
}

export enum SalaryRange {
  below40000 = "1$-60000$",
  from40000to60000 = "60000$-100000$",
  from60000to100000 = "100000$-150000$",
  above100000 = "150000$ >",
}

export enum InputNames {
  Email = "email",
  FirstName = "first_name",
  LastName = "last_name",
  Username = "username",
}

export enum JobInputNames {
  Title = "title",
  Email = "email",
  Address = "address",
  Salary = "salary",
  Position = "position",
  Company = "company",
  Experience = "experience",
}

export enum JobsByUser {
  Created = "Created",
  Applied = "Applied",
}

export const filters = {
  jobType: Object.values(JobType),
  education: Object.values(Education),
  industry: Object.values(Industry),
  salary: Object.values(SalaryRange),
  hidden: false,
};
