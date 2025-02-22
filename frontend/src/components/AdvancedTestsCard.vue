<script setup>
const props = defineProps({
  advancedTests: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(["update:advancedTests"]);

// Add Test Row to the advanced Tests
function addTestRow() {
  const newTest = { domain: "", type: "", condition: "" }; // Create a fresh object
  emit("update:advancedTests", [...props.advancedTests, newTest]);
}

// Remove test row from advancedTests
function removeTestRow(index) {
  if (props.advancedTests.length > 1) {
    const newTests = [...props.advancedTests];
    newTests.splice(index, 1);
    emit("update:advancedTests", newTests);
  }
}

// Update individual field in a test row
function updateField(index, field, value) {
  const newTests = [...props.advancedTests];
  newTests[index] = {
    ...newTests[index],
    [field]: value,
  };
  emit("update:advancedTests", newTests);
}

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
          Use the following section to test:-
        </p>
        <ol class="text-muted small-text-1 text-center">
          <li>Vocabulary Checks</li>
          <li>Simple Domain Standard Checks</li>
        </ol>
        <p class="text-muted small-text-1 m-3">
          For Vocabulary Checks, define comma separated values on each line for a single property
          where the first column represents the name and the second column the description.<br />
          For Standard Checks, mention the condition explicitly in 3–4 lines.
        </p>
      </div>
      <!-- Dynamic test rows container -->
      <div id="test-rows-container">
        <div class="row g-3" v-for="(test, index) in props.advancedTests" :key="index">
          <div class="col-1">
            <button
              type="button"
              class="btn btn-outline-danger"
              @click="removeTestRow(index)"
              :disabled="props.advancedTests.length === 1"
            >
              -
            </button>
          </div>
          <div class="col-3">
            <label class="form-label">Specify Your Domain</label>
            <input
              type="text"
              class="form-control"
              required
              v-model="test.domain"
              @input="updateField(index, 'domain', $event.target.value)"
              placeholder="Your Domain. Eg. Biological Sciences"
              style="font-size: 0.7em; text-align: center"
            />
          </div>
          <div class="col-2">
            <label class="form-label">Test Type</label>
            <select
              class="form-select"
              v-model="test.type"
              @change="updateField(index, 'type', $event.target.value)"
              style="font-size: 0.9em"
            >
              <option value="">Please select</option>
              <option>Vocabulary Check</option>
              <option>Standard Check</option>
            </select>
          </div>
          <div class="col-6">
            <label class="form-label">Condition</label>
            <textarea
              class="form-control"
              required
              rows="5"
              :placeholder="getPlaceholder(test.type)"
              v-model="test.condition"
              @input="updateField(index, 'condition', $event.target.value)"
              style="font-size: 0.8em"
            ></textarea>
          </div>
        </div>
      </div>
      <!-- Add new test row button -->
      <div>
        <button type="button" class="btn btn-outline-primary" @click="addTestRow">+</button>
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
