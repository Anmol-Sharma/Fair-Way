<script setup>
import { ref, watch } from "vue";

let advancedTests = ref([{ domain: "", type: "", condition: "" }]); // Initial empty row
const emit = defineEmits(["update:advancedTests"]);

// For the very first emit when the object is defined
emit("update:advancedTests", advancedTests.value);

const TestRows = 5;

// Add Test Row to the advanced Tests
function addTestRow() {
  if (advancedTests.value.length < TestRows) {
    advancedTests.value.push({ domain: "", type: "", condition: "" });
    emit("update:advancedTests", advancedTests.value);
  }
}

// Remove test row from advancedTests
function removeTestRow(index) {
  if (advancedTests.value.length > 1) {
    advancedTests.value.splice(index, 1);
    emit("update:advancedTests", advancedTests.value);
  }
}

// Watch for changes in the advancedTests array
watch(
  advancedTests,
  (newValue) => {
    emit("update:advancedTests", newValue);
  },
  { deep: true } // Enable deep watching to detect nested object changes
);

// Placeholder function for condition
function getPlaceholder(type) {
  if (type === "Vocabulary Check") {
    return "Eg:\n'Temporal Resolution', Describes the frequency or interval of data collection over time\n'Geospatial Extent', Geographic area covered by a dataset";
  } else if (type === "Standard Check") {
    return "Describe a single standard check here. Don't create complex instructions, Keep it simple in a manner which can be answered on metadata with true/false.";
  }
  return ""; // default placeholder
}
</script>

<template>
  <div class="card advanced-testing-card">
    <div class="card-body text-center">
      <div>
        <h5 class="card-title">Advanced User Defined Tests on Metadata</h5>
        <p class="text-muted small-text-1 m-3">
          LLMs can assist with checking your domain specific Vocabulary and Other Standards if
          carefully provided with instructions.<br />
          Use the following section to define any of the following <strong>(max. FIVE)</strong>:-
        </p>
        <ol class="text-muted small-text-1 text-center">
          <li>Vocabulary Checks</li>
          <li>Simple Domain Standard Checks</li>
        </ol>
        <p class="text-muted small-text-1 m-3">
          For Vocabulary Checks, define comma separated values on each line for a single property
          where the first column represents the name and the second column the description. Remove
          any additional commas in the description.<br />
          For Standard Checks, mention the condition explicitly in 3–4 lines.
        </p>
      </div>
      <!-- Dynamic test rows container -->
      <div id="test-rows-container">
        <div class="row g-3" v-for="(test, index) in advancedTests" :key="index">
          <div class="col-1">
            <button
              type="button"
              class="btn btn-outline-danger"
              @click="removeTestRow(index)"
              :disabled="advancedTests.length === 1"
            >
              -
            </button>
          </div>
          <div class="col-3">
            <label class="form-label" :for="'domain-' + index">Specify Your Domain</label>
            <input
              :id="'domain-' + index"
              type="text"
              class="form-control"
              required
              v-model="test.domain"
              placeholder="Your Domain. Eg. Biological Sciences"
              style="font-size: 0.7em; text-align: center"
            />
          </div>
          <div class="col-2">
            <label class="form-label" :for="'type-' + index">Test Type</label>
            <select
              class="form-select"
              :id="'type-' + index"
              v-model="test.type"
              style="font-size: 0.9em"
            >
              <option value="">Please select</option>
              <option>Vocabulary Check</option>
              <option>Standard Check</option>
            </select>
          </div>
          <div class="col-6">
            <label class="form-label" :for="'condition-' + index">Condition</label>
            <textarea
              class="form-control"
              :id="'condition-' + index"
              required
              rows="5"
              :placeholder="getPlaceholder(test.type)"
              v-model="test.condition"
              style="font-size: 0.8em"
              maxlength="3000"
            ></textarea>
          </div>
        </div>
      </div>
      <!-- Add new test row button -->
      <div class="mt-3">
        <button
          type="button"
          class="btn btn-outline-primary"
          @click="addTestRow"
          :disabled="advancedTests.length >= TestRows"
        >
          +
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.advanced-testing-card {
  min-width: 75vw;
  margin: 0 auto;
  min-height: 15em;
  height: auto;
}

.text-center ol {
  list-style-position: inside;
  padding-left: 0;
}
</style>
