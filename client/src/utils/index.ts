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

export { wait, slicer, getVisiblePages, defaultJob };
