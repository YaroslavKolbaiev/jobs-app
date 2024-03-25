<template>
  <div class="job-not-found">
    <h1>Job Not Found</h1>
    <p>The job you're looking for does not exist or has been removed.</p>
    <router-link to="/"> Go back to home </router-link>
  </div>
</template>

<style scoped>
.job-not-found {
  font-family: Poppins, sans-serif;
  color: var(--c-main-text);
  text-align: center;
  padding: 2rem;
}

.job-not-found h1 {
  margin-bottom: 1rem;
}

.job-not-found p {
  margin-bottom: 2rem;
}

.job-not-found a {
  color: var(--c-blue);
  text-decoration: none;
}
</style>
