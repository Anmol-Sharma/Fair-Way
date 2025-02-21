<script setup>
import { offlineAssessment, onlineAssessment } from "../utils/resultUtils.js";
import { validateVocabulary } from "../utils/helperUtils.js";
import { ref, toRaw } from "vue";
import { getConfig } from "../utils/config_loader.js";
const config = getConfig();

sessionStorage.clear();

let url = ref();

// Define variables to handle files for offline assessment
let Files = ref([]);
let metadataFile = ref();

// Define some conditional rendering variables
let onlineFlag = ref(true);
let offlineFlag = ref(false);
let advancedTesting = ref(false);

let advancedTests = ref([
  { domain: "", type: "", condition: "" }, // Initial empty row
]);

function addTestRow() {
  advancedTests.value.push({ domain: "", type: "" });
}

function removeTestRow(index) {
  if (advancedTests.value.length > 1) {
    advancedTests.value.splice(index, 1);
  }
}

function getPlaceholder(type) {
  if (type === "Vocabulary Check") {
    return "Eg:\n'Temporal Resolution', Describes the frequency or interval of data collection over time\n'Geospatial Extent', Geographic area covered by a dataset";
  } else if (type === "Standard Check") {
    return "Describe a single standard check here. Don't create complex instructions, Keep it simple in a manner which can be answered on metadata with true/false.";
  }
  return ""; // default placeholder
}

function getAdvancedTests() {
  // Only validate when advanced testing is enabled
  if (advancedTesting.value) {
    // Iterate over each advanced test row
    for (const test of advancedTests.value) {
      // Skip rows that are completely empty (allows the default single empty row)
      if (test.domain.trim() === "" && test.type.trim() === "" && test.condition.trim() === "") {
        continue;
      }
      // If any field is filled, then all must be filled
      if (test.domain.trim() === "" || test.type.trim() === "" || test.condition.trim() === "") {
        alert("Incomplete advanced test row. Please fill in Domain, Test Type, and Condition.");
        throw new Error("Incomplete advanced test row.");
      }
      // For Vocabulary Check, do additional validation on the condition
      if (test.type === "Vocabulary Check" && !validateVocabulary(test.condition)) {
        alert("Condition Not Satisfied for Vocabulary Test");
        throw new Error("Vocabulary Condition Not Satisfied");
      }
    }
  }

  // If there is only one row and it is completely empty, treat it as if no advanced test is defined.
  if (
    advancedTests.value.length === 1 &&
    advancedTests.value[0].domain.trim() === "" &&
    advancedTests.value[0].type.trim() === "" &&
    advancedTests.value[0].condition.trim() === ""
  ) {
    return [];
  }

  return advancedTests.value;
}

// Helper function which triggers when the file input changes.
function offlinePreprocess(event) {
  const validType = config.global["supported_metadata_file_types"];

  onlineFlag.value = false;
  offlineFlag.value = true;

  const files = Array.from(event.target.files);
  // Filter files based on extensions and only allow supported metadata file types
  const filteredFiles = files.filter((file) => {
    const extension = "." + file.name.split(".").pop().toLowerCase();
    return validType.includes(extension);
  });

  Files.value = filteredFiles;
}

function onlineAssess(event, resourceUrl) {
  const doiPattern = /^(?:https?:\/\/)?doi\.org\/10\.\d+\/(?:dryad|zenodo)(?:\.[\w-]+)*$/;
  const zenodoPattern = /^(https?:\/\/)?zenodo\.org\/records\/\d+$/;
  const dryadPattern =
    /^(https?:\/\/)datadryad\.org\/stash\/dataset\/doi:10\.\d+\/dryad\.[a-zA-Z0-9-]+$/;

  if (
    !doiPattern.test(resourceUrl) &&
    !zenodoPattern.test(resourceUrl) &&
    !dryadPattern.test(resourceUrl)
  ) {
    alert(
      "Invalid Record. Only valid DOIs published by Zenodo or Dryad accepted or Enter valid url of a Zenodo or Dryad Record."
    );
  } else {
    // send back the url to backend for processing
    try {
      const tests = getAdvancedTests();
      onlineAssessment({ url: resourceUrl, advancedTests: toRaw(tests) });
    } catch (e) {
      // TODO: Handle if advanced tests conditions aren't satisfied for both online and offline assessment forms
    }
  }
  url.value = "";
}
</script>

<template>
  <div class="container-fluid main-container">
    <div class="row-cols-1">
      <div class="col d-flex justify-content-center">
        <h1 style="font-size: 2.5rem; margin: 1.5rem">FAIR Assessment</h1>
      </div>
    </div>
    <div class="row-cols-1">
      <div class="col d-flex justify-content-center">
        <p>
          Programatically check FAIRness of research data sets. You have two options available
          below.
          <br />
          You can either enter a DOI url or a URL from following supported data repositories:
          <strong>Dryad</strong>, <strong>Zenodo</strong>, <strong>Hugging Face</strong> OR you can
          upload your local metadata files for assessment.
        </p>
      </div>
    </div>
    <div class="row g-4 justify-content-center">
      <div class="col-6" v-if="onlineFlag">
        <div class="card">
          <div class="card-body text-center">
            <h5 class="card-title">Online / Published Dataset</h5>
            <p>Enter Valid DOI of dataset from defined Data Repositories above.</p>
            <!-- TODO: Add support for hugging face datasets -->
            <form @submit.prevent="onlineAssess($event, toRaw(url))">
              <div class="my-4 d-flex justify-content-center">
                <div class="input-group w-75">
                  <input
                    type="text"
                    class="form-control"
                    aria-describedby="basic-addon3 basic-addon4"
                    placeholder="DOI of the dataset"
                    style="text-align: center"
                    id="dataset_url"
                    required
                    v-model="url"
                  />
                </div>
              </div>
              <div class="text-center">
                <button type="submit" class="btn btn-primary">Start Assessment</button>
              </div>
              <!-- Add help section with examples -->
              <div class="mt-4 text-center" v-if="onlineFlag">
                <p class="text-muted fs-6">Not sure what to test? Try the example below:</p>
                <div class="mt-1">
                  <a
                    href="https://doi.org/10.5061/dryad.ngf1vhj3t"
                    target="_blank"
                    class="text-decoration-none text-muted fs-6"
                  >
                    Example (Dryad Dataset) : https://doi.org/10.5061/dryad.ngf1vhj3t
                  </a>
                  <br />
                  Copy and Paste this link above and start assessment
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div class="col-6">
        <div class="card">
          <div class="card-body text-center">
            <h5 class="card-title">Offline / Unpublished Dataset</h5>
            <p class="card-text">Select your Local/ Unpublished data sources.</p>

            <!-- pass raw js object for files and metadata selected file. -->
            <form
              @submit.prevent="
                offlineAssessment(
                  $event,
                  toRaw(Files),
                  toRaw(metadataFile),
                  toRaw(getAdvancedTests())
                )
              "
            >
              <div class="d-flex justify-content-center mt-4 mb-3 ms-5" v-if="onlineFlag">
                <input type="file" webkitdirectory required @change="offlinePreprocess" />
              </div>
              <div class="min-height: 75vh;" v-if="offlineFlag">
                <br />
                <p class="card-text">Detected Metadata Files:-</p>
                <ul class="list-inline">
                  <li v-for="file in Files">
                    {{ file.name }}
                  </li>
                </ul>
                <div class="my-2 d-flex justify-content-center">
                  <label for="file-select">Choose Metadata file</label>
                  <select
                    class="form-select form-select-sm w-50 mx-3"
                    name="Metadata File"
                    id="file-select"
                    v-model="metadataFile"
                    required
                  >
                    <option v-for="(file, index) in Files" v-bind:value="index">
                      {{ file.name }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="text-center">
                <button type="submit" class="btn btn-primary my-3" id="start-offline-assess">
                  Start Assessment
                </button>
              </div>
              <!-- Add help section with example files -->
              <div class="mt-1 text-center" v-if="!offlineFlag">
                <p class="text-muted fs-6">
                  Not sure what to test? Try these example metadata files:
                </p>
                <div class="mt-1">
                  <div class="d-flex flex-column flex-md-row gap-3 justify-content-center">
                    <!-- Example File 1 -->
                    <div class="example-file-card">
                      <h6>Example JSON Metadata File</h6>
                      <a
                        href="/example_files/example_metadata_1.json"
                        download="example_metadata.json"
                        class="btn btn-outline-secondary btn-sm mt-2"
                      >
                        <i class="bi bi-download"></i> Download
                      </a>
                    </div>

                    <!-- Example File 2 -->
                    <div class="example-file-card">
                      <h6>Example XML Metadata File</h6>
                      <a
                        href="/example_files/example_metadata_2.xml"
                        download="example_metadata.xml"
                        class="btn btn-outline-secondary btn-sm mt-2"
                      >
                        <i class="bi bi-download"></i> Download
                      </a>
                    </div>

                    <!-- Example File 3 -->
                    <div class="example-file-card">
                      <h6>Example README Metadata File</h6>
                      <a
                        href="/example_files/example_metadata_3.md"
                        download="example_metadata.md"
                        class="btn btn-outline-secondary btn-sm mt-2"
                      >
                        <i class="bi bi-download"></i> Download
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div class="row justify-content-center my-3">
      <div class="col-auto">
        <div class="form-check text-center my-2">
          <label class="form-label" id="advanced-testing-label"
            ><strong>Advanced Testing</strong></label
          >
          <input type="checkbox" class="form-check-input" v-model="advancedTesting" />
        </div>
      </div>
    </div>
    <div class="row-cols-1 mb-5" v-if="advancedTesting">
      <div class="col-12 d-flex justify-content-center">
        <div class="card advanced-testing-card">
          <div class="card-body text-center">
            <h5 class="card-title">Advanced User Defined Tests on Metadata</h5>
            <p class="text-muted fs-5 m-3">
              LLMs can assist with checking your domain specific Vocabulary and Other Standards if
              carefully provided with instructions.<br />
              Use the following section to test:-
            </p>
            <ol class="text-muted fs-5 text-center">
              <li>Vocabulary Checks</li>
              <li>Simple Domain Standard Checks</li>
            </ol>
            <p class="text-muted fs-5 m-3">
              For Vocabulary Checks, define comma separated values on each line for a single
              property where first column represents name and second columnd represents property
              description.<br />
              For Standard Checks, Mention the condition explicitly in max 3-4 lines.
            </p>
            <!-- Dynamic test rows container -->
            <div id="test-rows-container">
              <!-- Initial test row -->
              <div class="row g-3" v-for="(test, index) in advancedTests" :key="index">
                <div class="col-md-1">
                  <button
                    type="button"
                    class="btn btn-outline-danger"
                    @click="removeTestRow(index)"
                    :disabled="advancedTests.length === 1"
                  >
                    <i class="bi bi-dash-md" style="font-size: 1.1em">-</i>
                  </button>
                </div>
                <div class="col-md-3">
                  <label class="form-label">Specify Your Domain</label>
                  <input
                    type="text"
                    class="form-control"
                    required
                    v-model="test.domain"
                    placeholder="Your Domain. Eg. Biological Sciences"
                    style="font-size: 0.7em; text-align: center"
                  />
                </div>
                <div class="col-md-2">
                  <label class="form-label">Test Type</label>
                  <select class="form-select" v-model="test.type" style="font-size: 0.9em">
                    <option value="">Please select</option>
                    <option>Vocabulary Check</option>
                    <option>Standard Check</option>
                  </select>
                </div>
                <div class="col-md-6">
                  <label class="form-label">Condition</label>
                  <textarea
                    class="form-control"
                    id="feedbackText"
                    required
                    rows="4"
                    :placeholder="getPlaceholder(test.type)"
                    v-model="test.condition"
                    style="font-size: 0.8em"
                  ></textarea>
                </div>
              </div>
            </div>

            <!-- Add new test row button -->
            <div class="text-center my-2">
              <button type="button" class="btn btn-outline-primary" @click="addTestRow">
                <i class="bi bi-plus-md" style="font-size: 1.1em"></i> +
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-container {
  margin-bottom: 3.5rem;
  min-height: 80vh;
}

.text-muted {
  color: #6c757d !important;
}

.fs-5 {
  font-size: 0.775rem !important;
}

.fs-6 {
  font-size: 0.875rem !important;
}

.main-container p {
  font-size: 1.2em;
}

.btn {
  position: relative;
}

#advanced-testing-label {
  font-size: 1.2em;
}

/* Increase checkbox size */
.form-check-input {
  width: 1.2em;
  height: 1.2em;
}

/* Optional: Add some styling to make it look better */
.form-check-input {
  border-radius: 0.35em;
  transition: all 0.2s ease-in-out;
}

.form-check-input:hover {
  border-color: #80bdff;
}

.form-check-input:checked {
  background-color: #0d6efd;
  border-color: #0d6efd;
}

.card {
  height: 25em;
  max-width: 45vw;
}

.example-file-card {
  background-color: #f8f9fa;
  padding: 12px;
  border-radius: 5px;
  text-align: center;
}

.bi-download {
  margin-right: 4px;
}

.row {
  margin-top: 0.6em;
}

/* New styles for advanced testing card */
.advanced-testing-card {
  min-width: 75vw; /* Set width to 75% of view width */
  margin: 0 auto; /* Center the card horizontally */
  min-height: 15em;
  height: auto;
}
.text-center ol {
  list-style-position: inside;
  padding-left: 0;
}
</style>
