<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid d-flex align-items-center">
      <RouterLink class="navbar-brand d-flex align-items-center" to="/">
        <img
          src="../assets/llama_fair.jpg"
          alt="Logo"
          width="30"
          height="30"
          class="d-inline-block me-2"
        />
        FAIR-Way
      </RouterLink>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <RouterLink class="nav-link" to="/About">About</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/Assess">Assess</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/Enrichment">Enrichment</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/Docs">Docs</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/Feedback">General Feedback</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/Survey">Survey Feedback</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  background-color: #e6e8eb;
  max-height: 60px;
}

.nav-item {
  text-align: center;
  font-size: 1.1rem;
  margin: 0.2rem;
}

.navbar-brand {
  font-size: 1.3rem;
  display: flex;
  align-items: center;
}

.nav-link {
  font-size: 1.2rem;
}
</style>
