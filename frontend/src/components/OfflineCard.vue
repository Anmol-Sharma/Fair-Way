<script setup>
import { ref } from "vue";

// Read global config
import { getConfig } from "../utils/config_loader.js";
const config = getConfig();

// Define props to handle
const props = defineProps({
  showOnlineFlag: {
    type: Boolean,
    required: true,
  },
  showOfflineFlag: {
    type: Boolean,
    required: true,
  },
});

// Define update Emits
const emit = defineEmits(["update:showOnlineFlag", "update:showOfflineFlag", "formSubmit"]);

let metadataFile = ref();
let Files = ref([]);

// Helper function which triggers when the file input changes.
function offlinePreProcess(event) {
  const validType = config.global["supported_metadata_file_types"];

  const allFiles = Array.from(event.target.files);
  // Filter files based on extensions and only allow supported metadata file types
  const filteredFiles = allFiles.filter((file) => {
    const extension = "." + file.name.split(".").pop().toLowerCase();
    return validType.includes(extension);
  });

  if (filteredFiles.length < 1) {
    alert("No relevant Metadata Files found, please select another directory.");
    return;
  }

  // Emit updates instead of modifying props directly, since props are readOnly
  emit("update:showOnlineFlag", false);
  emit("update:showOfflineFlag", true);

  // Update the Files ref
  Files.value = filteredFiles;
}
</script>
<template>
  <div class="card">
    <div class="card-body text-center">
      <h5 class="card-title">Offline / Unpublished Dataset</h5>
      <p class="card-text">Select your Local/ Unpublished data sources.</p>
      <form @submit.prevent="$emit('formSubmit', Files, metadataFile)">
        <div class="d-flex justify-content-center mt-4 mb-3 ms-5" v-if="props.showOnlineFlag">
          <input type="file" webkitdirectory required @change="offlinePreProcess" />
        </div>
        <div v-if="props.showOfflineFlag">
          <br />
          <p class="card-text">Detected Metadata Files:-</p>
          <ul class="list-inline">
            <li v-for="file in Files" :key="file.name">
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
        <div class="mt-1 text-center" v-if="!props.showOfflineFlag">
          <p class="text-muted small-text-2">
            Not sure what to test? Try these example metadata files below. Simply Download and use
            for Assessment.
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
</template>

<style scoped>
.card {
  min-height: 27em;
  height: auto;
  max-width: 55vw;
}

p {
  font-size: 1.2em;
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
</style>
