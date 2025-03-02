<script setup>
import router from "../router";
sessionStorage.clear();
</script>

<template>
  <div class="main-container container-fluid d-flex justify-content-center align-items-center">
    <div class="d-flex flex-column align-items-center p-3">
      <div class="d-flex align-items-center">
        <img src="../assets/llama_fair.jpg" alt="Logo" width="192" height="192" class="me-4" />
        <h1>FAIR-Way</h1>
      </div>
      <br />
      <p class="text-center mb-4">
        Web-App to assess FAIRness of Research Datasets & assist with Metadata Enrichment using the
        Power of LLMs.
        <br />
        Read more about the tool and its working in the
        <RouterLink class="link-primary" to="/About">About</RouterLink> Section.
      </p>
      <div class="d-flex justify-content-center">
        <button
          type="button"
          class="btn btn-primary btn-lg"
          @click="router.push({ name: 'Assess' })"
        >
          Start FAIR Assessment
        </button>
        <button
          type="button"
          class="btn btn-primary btn-lg"
          @click="router.push({ name: 'Enrichment' })"
        >
          Metadata Enrichment
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-container {
  max-width: 80vw;
}
</style>
