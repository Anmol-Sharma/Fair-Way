<script setup></script>

<template>
  <div class="container-fluid main-container justify-content-center p-5" id="about-section">
    <h1>About</h1>
    <section id="overview">
      <h2>Overview</h2>
      <p>
        Welcome to <strong>FAIR-Way</strong>, an advanced web service designed to automatically
        assess the FAIRness of digital research datasets. Leveraging the power of Large Language
        Models (LLMs), our platform performs a comprehensive series of tests on your datasets and
        combines their results to provide a detailed and accurate FAIRness summary. <br />
        <br />

        The FAIR Data Principles are a set of guidelines designed to improve the findability,
        accessibility, interoperability, and reusability of digital assets. These principles are
        particularly important in the context of scientific research data, but they can be applied
        to any type of digital information. <br />
        <br />

        Inspired by tools like <a href="https://www.f-uji.net/index.php?action=about#">F-UJI</a> and
        <a href="https://fair-checker.france-bioinformatique.fr/">FAIR-Checker</a> for automated
        FAIR-testing, we would like to extend FAIR automated testing to next level by utilizing
        LLMs.
      </p>
      <h3>Key Features:</h3>
      <ul>
        <li>
          <strong>Automated Assessment</strong>: Utilizes advanced LLMs to evaluate datasets against
          the FAIR principles. We utilize <a href="https://www.fairsfair.eu/">FAIRsFAIR</a> domain
          agnostic tests as baseline.
        </li>
        <li>
          <strong>Detailed Summary</strong>: Provides a consolidated report highlighting strengths
          and areas for improvement.
        </li>
        <li>
          <strong>User-Friendly Interface</strong>: Easy-to-use interface for uploading datasets and
          viewing results.
        </li>
      </ul>
      Cite our works as:- (TODO: Coming soon)
    </section>
    <br />

    <section id="Usage">
      <h2>Usage</h2>
      <p>
        In order to assess, FAIRness of data objects, navigate to
        <RouterLink class="link-primary" to="/Assess">Assess</RouterLink> section and you have two
        options. You can either assess an online / published resource from
        <a href="https://zenodo.org/">Zenodo</a> or <a href="https://dryad.org/">Dryad</a> data
        repositories or you can also perform analysis on you local metadata file.
      </p>
      <h3>Data Formats:</h3>
      <ul>
        <li>
          Supported common data formats include
          <strong>plaintext, markdown, json, json-ld, xml, html, xhtml</strong>.
        </li>
        <li>File sizes upto 100MB are supported</li>
      </ul>
    </section>

    <section id="scope-constraints">
      <h2>Scope, Constraints and Limitations</h2>
      <p>
        <strong>Fair-Way</strong> is designed to support a wide range of datasets across various
        domains and from various sources. While there exists Some aspects (rich, plurality,
        accurate, relevant) specified in FAIR principles still require human mediation and
        interpretation which other automated tools cannot easily test with explicitly programmed
        logic, using LLMs can help with these tasks and should be able to perform these tests close
        to human level.
      </p>
      <!-- TODO: Update the cleanup the about section at the end -->
      <!-- <h3>Metadata Standards:</h3>
      <ul>
        <li>
          Evaluates metadata according to standards like Dublin Core, DataCite Metadata Schema, and
          domain-specific ontologies.
        </li>
      </ul> -->
      <!-- <h3>Interoperability Checks:</h3>
      <ul>
        <li>Assesses compatibility with various systems and APIs.</li>
      </ul>
      <h3>Accessibility Verification:</h3>
      <ul>
        <li>Ensures datasets are accessible via well-documented APIs or download services.</li>
      </ul> -->
      <h3>Data Privacy and Security:</h3>
      <ul>
        <li>
          <strong>Data Handling</strong>: Uploaded datasets are processed securely and deleted after
          evaluation to ensure privacy.
        </li>
      </ul>
      <h3>Evaluation Accuracy:</h3>
      <ul>
        <li>
          <strong>Contextual Understanding</strong>: LLMs provide valuable insights but may
          sometimes misinterpret complex or ambiguous data structures. Please double check the
          results to be sure.
        </li>
      </ul>
      <h3>Scope of Evaluation:</h3>
      <ul>
        <li>
          <strong>Domain-Specific Tests</strong>: Some tests are more relevant to specific domains
          and may not cover all aspects for datasets outside these areas.
        </li>
        <li>
          <strong>Continuous Improvement</strong>: The service is continually improving based on
          user feedback and advancements in LLM technology.
        </li>
      </ul>
    </section>
  </div>
</template>

<style scoped>
.main-container h1,
h2,
h3 {
  color: #333;
}

.main-container h1 {
  font-size: 3.5em;
}

.main-container p {
  font-size: 1.2em;
  text-align: left;
}

ul {
  list-style-type: disc;
  margin-left: 1.4em;
  font-size: 1.1em;
}

#about-section {
  font-family: Arial, sans-serif;
}
</style>
