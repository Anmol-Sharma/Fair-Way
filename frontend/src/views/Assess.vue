<script setup>
import { offlineAssessment, onlineAssessment } from "../utils/resultUtils.js";
import { validateVocabulary } from "../utils/helperUtils.js";
import { ref, toRaw } from "vue";
import AdvancedTestsCard from "../components/AdvancedTestsCard.vue";
import OfflineCard from "../components/OfflineCard.vue";
import OnlineCard from "../components/OnlineCard.vue";

sessionStorage.clear();

// Define some conditional rendering variables
let showOnlineFlag = ref(true);
let showOfflineFlag = ref(false);
let advancedTestingFlag = ref(false);
let advancedTests = ref([]);

// TODO: Handle bakar for this function
function getAdvancedTests() {
  // Only validate when advanced testing is enabled
  if (advancedTestingFlag.value) {
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

const submitOnlineRequest = (resourceUrl) => {
  // send back the url to backend for processing
  try {
    const tests = getAdvancedTests();
    onlineAssessment({ url: resourceUrl, advancedTests: toRaw(tests) });
  } catch (e) {
    // TODO: Handle if advanced tests conditions aren't satisfied for both online and offline assessment forms
  }
};
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
      <div class="col-6" v-if="showOnlineFlag">
        <OnlineCard :show-online-flag="showOnlineFlag" @formSubmit="submitOnlineRequest" />
      </div>
      <div class="col-6">
        <OfflineCard
          v-model:showOnlineFlag="showOnlineFlag"
          v-model:showOfflineFlag="showOfflineFlag"
          @formSubmit="
            (Files, metadataFile) => {
              offlineAssessment(Files, metadataFile, getAdvancedTests());
            }
          "
        ></OfflineCard>
      </div>
    </div>
    <div class="row justify-content-center my-3">
      <div class="col-auto">
        <div class="form-check text-center my-2">
          <label class="form-label mx-1" id="advanced-testing-label"
            ><strong>Advanced Testing?</strong></label
          >
          <input type="checkbox" class="form-check-input" v-model="advancedTestingFlag" />
        </div>
      </div>
    </div>
    <div class="row-cols-1 mb-5" v-if="advancedTestingFlag">
      <div class="col-12 d-flex justify-content-center">
        <AdvancedTestsCard v-model:advancedTests="advancedTests"></AdvancedTestsCard>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-container {
  margin-bottom: 3.5rem;
  min-height: 80vh;
}

.main-container p {
  font-size: 1.2em;
}

.row {
  margin-top: 0.5em;
}

/*
###########################################
#   Styles for Advanced Testin Checkmark  #
###########################################
*/

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
</style>
