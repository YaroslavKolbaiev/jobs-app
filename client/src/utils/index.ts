function wait(delay: number) {
  return new Promise<void>((resolve) => {
    setTimeout(resolve, delay);
  });
}

function slicer(chars: number, str: string | null) {
  const isLongString = str.length > chars;

  return isLongString ? str?.slice(0, chars) + '...' : str;
}

export { wait, slicer };
