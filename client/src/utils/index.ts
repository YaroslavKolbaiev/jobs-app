import { JobType, Education, Industry, SalaryRange } from '@/enums';

function wait(delay: number) {
  return new Promise<void>((resolve) => {
    setTimeout(resolve, delay);
  });
}

function slicer(chars: number, str: string) {
  const isLongString = str.length > chars;

  return isLongString ? str?.slice(0, chars) + '...' : str;
}

function getVisiblePages(current: number, total: number) {
  if (total <= 7) {
    return range(total);
  }
  if (current < 5) {
    return [...range(5), '...', total];
  }
  if (current > total - 4) {
    return [1, '...', ...range(5, total - 4)];
  }
  return [1, '...', current - 1, current, current + 1, '...', total];
}

function range(count: number, start = 1) {
  return Array.from(new Array(count), (x, i) => i + start);
}

function salaryParser(salary: string) {
  let result = [];
  if (salary.includes('-')) {
    result = salary.split('-').map((s) => s.trim().slice(0, -1));
    return result;
  }

  salary = salary.split('>')[0].trim().slice(0, -1);

  result = [salary, ''];

  return result;
}

function getCookie(id: string) {
  const value = document.cookie.match('(^|;)?' + id + '=([^;]*)(;|$)');
  return value ? unescape(value[2]) : null;
}

function validateEmail(value: string) {
  if (!value) {
    return 'Email is required';
  }

  const emailPattern = /^[\w.+-]+@([\w-]+\.){1,3}[\w-]{2,}$/;

  if (!emailPattern.test(value)) {
    return 'Email is not valid';
  }
}

function validatePassword(value: string) {
  if (!value) {
    return 'Password is required';
  }

  if (value.length < 6) {
    return 'At least 6 characters';
  }
}

const filters = {
  jobType: Object.values(JobType),
  education: Object.values(Education),
  industry: Object.values(Industry),
  salary: Object.values(SalaryRange),
  hidden: false,
};

export {
  wait,
  slicer,
  getVisiblePages,
  salaryParser,
  getCookie,
  validateEmail,
  validatePassword,
  filters,
};
