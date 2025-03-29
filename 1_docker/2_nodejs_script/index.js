const interval = setInterval(() => {
  const now = new Date();
  console.log(now.toLocaleTimeString());
}, 1000);

// Stop after 1 minute (60 seconds)
setTimeout(() => {
  clearInterval(interval);
  console.log("Finished after 1 minute.");
}, 60 * 1000);
