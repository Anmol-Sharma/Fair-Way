<script setup></script>

<template>
  <div class="container-fluid main-container justify-content-center p-5" id="about-section">
    <h1>About</h1>
    <br />
    <section id="overview">
      <h2>Overview</h2>
      <p>
        Welcome to <strong>Fair-Way</strong>, an open-source web application designed to automate
        and enhance the assessment of FAIRness for digital research datasets. Built on the power of
        Large Language Models (LLMs), Fair-Way evaluates datasets against the
        <a href="https://www.fairprinciples.org/">FAIR Data Principles</a>, providing actionable
        insights to improve the findability, accessibility, interoperability, and reusability of
        research data.
      </p>
      <p>
        The FAIR Data Principles are a set of guidelines aimed at making digital research data more
        accessible and usable for both humans and machines. While some existing tools like
        <a href="https://www.f-uji.net/index.php?action=about#">F-UJI</a> and
        <a href="https://fair-checker.france-bioinformatique.fr/">FAIR-Checker</a> offer automated
        FAIR assessments, they often face limitations in handling diverse metadata formats,
        domain-specific requirements, and complex data structures. Fair-Way tries to address some
        these gaps by leveraging LLMs to deliver a more flexible, scalable, and accurate solution.
      </p>
    </section>

    <section id="key-features">
      <h2>Key Features</h2>
      <ul>
        <li>
          <strong>LLM-Powered FAIR Assessment</strong>: Utilizes Large Language Models (e.g.,
          GPT-4o, Mistral-small) to evaluate datasets against FAIR metrics, including
          domain-agnostic and domain-specific tests.
        </li>
        <li>
          <strong>Comprehensive Metadata Support</strong>: Handles structured (JSON, XML, etc.) and
          unstructured metadata formats, including published datasets from repositories like
          <a href="https://zenodo.org/">Zenodo</a> and <a href="https://dryad.org/">Dryad</a>, as
          well as local files.
        </li>
        <!-- <li>
          <strong>Divide-and-Conquer Strategy</strong>: Breaks down complex metadata into manageable
          chunks for accurate LLM processing, avoiding context window limitations and reducing
          hallucinations.
        </li> -->
        <li>
          <strong>Domain-Specific Customization</strong>: Allows users to define custom tests for
          vocabulary checks or domain-specific standards via user-provided prompts.
        </li>
        <li>
          <strong>Detailed FAIRness Reports</strong>: Generates consolidated summaries highlighting
          FAIR scores and provides detailed feedback on various metrics.
        </li>
        <li>
          <strong>Open Source & Scalable</strong>: Designed for cross-domain applicability, with
          code and evaluation datasets available on
          <a href="https://github.com/Anmol-Sharma/Fair-Way">GitHub</a>.
        </li>
      </ul>
    </section>

    <section id="how-it-works">
      <h2>How Fair-Way Works</h2>
      <p>Fair-Way follows a systematic workflow to assess FAIRness:</p>
      <ol>
        <li>
          <strong>Metadata Ingestion</strong>: Upload datasets or provide URLs to online
          repositories (e.g., Zenodo, Dryad).
        </li>
        <li>
          <strong>Preprocessing</strong>: Cleans and validates metadata, reducing token counts for
          efficient LLM processing.
        </li>
        <li>
          <strong>Chunking & Task Decomposition</strong>: Splits large metadata into smaller parts
          and breaks down FAIR metrics into simpler, task-specific prompts.
        </li>
        <li>
          <strong>LLM Analysis</strong>: Evaluates each chunk using tailored prompts, few-shot
          examples, and structured output formats (e.g., JSON) to ensure consistency.
        </li>
        <li>
          <strong>Result Aggregation</strong>: Combines chunked results into a unified FAIRness
          report, including domain-specific tests and recommendations.
        </li>
      </ol>
    </section>

    <section id="usage">
      <h2>Usage</h2>
      <p>
        To assess FAIRness, navigate to the
        <RouterLink class="link-primary" to="/Assess">Assess</RouterLink> section. You can:
      </p>
      <ul>
        <li>
          <strong>Evaluate Published Data</strong>: Analyze datasets from
          <a href="https://zenodo.org/">Zenodo</a> or <a href="https://dryad.org/">Dryad</a> or
          <a href="https://huggingface.co/datasets">HuggingFace</a> using their URLs.
        </li>
        <li>
          <strong>Analyze Local Files</strong>: Upload metadata files in supported formats
          (plaintext, markdown, JSON, XML, HTML, etc.).
        </li>
      </ul>
      <h3>Supported Data Formats:</h3>
      <ul>
        <li><strong>Structured</strong>: JSON, JSON-LD, XML, HTML, XHTML.</li>
        <li><strong>Unstructured</strong>: Markdown, plaintext.</li>
      </ul>
      <!-- Highlighted Upload Limit Note -->
      <div class="upload-limit">
        <p><strong>Note:</strong> Metadata File sizes up to 100MB are supported.</p>
      </div>
    </section>

    <section id="scope-and-limitations">
      <h2>Scope, Constraints, and Limitations</h2>
      <p>
        Fair-Way is designed to support a wide range of datasets across scientific and
        non-scientific domains. While it excels in automating FAIR assessments, some aspects of the
        principles (e.g., contextual interpretation of ambiguous data) still require human
        oversight.
      </p>
      <h3>Key Constraints:</h3>
      <ul>
        <li>
          <strong>LLM Limitations</strong>: Reliance on LLMs may introduce hallucinations (e.g.
          false positives). Results should be reviewed for accuracy.
        </li>
        <li>
          <strong>Computational Demands</strong>: LLMs require significant resources, which may
          affect performance on low-end GPU hardware.
        </li>
        <li>
          <strong>Domain-Specific Gaps</strong>: While customizable, some niche domain standards may
          require additional user input or updates to the tool.
        </li>
      </ul>
    </section>

    <section id="why-fair-way">
      <h2>Why Choose Fair-Way?</h2>
      <p>Unlike traditional FAIR assessment tools, Fair-Way offers:</p>
      <ul>
        <li>
          <strong>Data Privacy</strong>: Uploaded datasets are processed securely and deleted after
          evaluation to ensure privacy.
        </li>
        <li>
          <strong>Greater Flexibility</strong>: Adapts to diverse metadata formats and
          domain-specific requirements without explicit programming.
        </li>
        <li>
          <strong>Improved Accuracy</strong>: Outperforms tools like F-UJI in metrics for
          accessibility and reusability.
        </li>
        <li>
          <strong>Future-Ready Design</strong>: Lays the groundwork for hybrid models combining LLMs
          with explicit logic to further enhance precision.
        </li>
      </ul>
    </section>

    <section id="citation">
      <h2>Citation</h2>
      <p>
        Please cite Fair-Way as:
        <br />
        <!-- <em
          >Anmol Sharma et al. "Fair-Way: Automating FAIRness Assessment with Large Language
          Models." [Conference/Journal Name], [Year].</em
        > -->
        <!-- <br /> -->
        (Citation details to be finalized; check back for updates.)
      </p>
    </section>

    <section id="get-involved">
      <h2>Get Involved</h2>
      <p>
        Fair-Way is an open-source project. Explore the code, contribute to development, or report
        issues on our <a href="https://github.com/Anmol-Sharma/Fair-Way">GitHub repository</a>.
        <!-- <br />
        Test Fair-Way live at
        <a href="https://hidden-for-double-blind.com/">[Testing Link]</a> (double-blind review
        version). -->
      </p>
    </section>
  </div>
</template>

<style scoped>
.main-container {
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
}

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
  /* max-width: 100px */
}

ul {
  list-style-type: disc;
  margin-left: 1.4em;
  font-size: 1.1em;
}

ol {
  list-style-type: disc;
  margin-left: 1.4em;
  font-size: 1.1em;
}

#about-section {
  font-family: Arial, sans-serif;
}

.upload-limit {
  background-color: #fff3cd; /* Light yellow */
  border-left: 4px solid #ffc107; /* Amber border */
  padding: 1rem;
  margin-top: 1.5rem;
  margin-bottom: 1.5rem;
  font-weight: bold;
  color: #856404; /* Darker text for contrast */
}
</style>
