function wait(delay: number) {
  return new Promise<void>((resolve) => {
    setTimeout(resolve, delay);
  });
}

function slicer(chars: number, str: string) {
  const isLongString = str.length > chars;

  return isLongString ? str?.slice(0, chars) + '...' : str;
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

export { wait, slicer, salaryParser };
