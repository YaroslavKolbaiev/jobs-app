<template>
  <div class="job-not-found">
    <h1>Jobs Not Found</h1>
    <p>There are no jobs for the provided query.</p>
    <router-link to="/">
      Go back to home
    </router-link>
  </div>
</template>

<style scoped>
.job-not-found {
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
