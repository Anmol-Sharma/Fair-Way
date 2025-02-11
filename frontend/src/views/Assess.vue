<script setup>
import { offline_assessment, online_assessment } from "../utils/result_utils.js";
import { ref, toRaw } from "vue";
import { getConfig } from "../utils/config_loader.js";
const config = getConfig();

sessionStorage.clear();

let url = ref();

// Define variables to handle files for offline assessment
let Files = ref([]);
let metadata_file = ref();

// Define some conditional rendering variables
let online_flag = ref(true);
let offline_flag = ref(false);

// Helper function which triggers when the file input changes.
function offline_preprocess(event) {
  const validType = config.global["supported_metadata_file_types"];

  online_flag.value = false;
  offline_flag.value = true;

  const files = Array.from(event.target.files);
  // Filter files based on extensions and only allow supported metadata file types
  const filteredFiles = files.filter((file) => {
    const extension = "." + file.name.split(".").pop().toLowerCase();
    return validType.includes(extension);
  });

  Files.value = filteredFiles;
}
function online_assess(event, url) {
  const pattern_doi = /^(?:https?:\/\/)?doi\.org\/10\.\d+\/(?:dryad|zenodo)(?:\.[\w-]+)*$/;
  const pattern_zenodo = /^(https?:\/\/)?zenodo\.org\/records\/\d+$/;
  const pattern_dryad =
    /^(https?:\/\/)datadryad\.org\/stash\/dataset\/doi:10\.\d+\/dryad\.[a-zA-Z0-9-]+$/;

  if (!pattern_doi.test(url) && !pattern_zenodo.test(url) && !pattern_dryad.test(url)) {
    alert(
      "Invalid Record. Only valid DOIs published by Zenodo or Dryad accepted or Enter valid url of a Zenodo or Dryad Record."
    );
  } else {
    // send back the url to backend for processing
    online_assessment(url);
  }
  this.url = "";
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
      <div class="col-6" v-if="online_flag">
        <div class="card">
          <div class="card-body text-center">
            <h5 class="card-title">Online / Published Dataset</h5>
            <p>Enter Valid DOI of dataset from defined Data Repositories above.</p>
            <!-- TODO: Add support for hugging face datasets -->
            <form @submit.prevent="online_assess($event, toRaw(url))">
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
              <div class="mt-4 text-center" v-if="online_flag">
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
            <form @submit.prevent="offline_assessment($event, toRaw(Files), toRaw(metadata_file))">
              <div class="d-flex justify-content-center mt-4 mb-3 ms-5" v-if="online_flag">
                <input type="file" webkitdirectory @change="offline_preprocess" />
              </div>
              <div class="min-height: 75vh;" v-if="offline_flag">
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
                    v-model="metadata_file"
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
              <div class="mt-1 text-center" v-if="!offline_flag">
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

.fs-6 {
  font-size: 0.875rem !important;
}

.main-container p {
  font-size: 1.2em;
}

.btn {
  position: relative;
}

.card {
  height: 30em;
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
  margin-top: 1rem;
}
</style>
