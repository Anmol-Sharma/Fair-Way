<script setup>
import Accordion from "../components/Accordion.vue";
import { onMounted, onUnmounted } from "vue";
import { ref } from "vue";
import { redirectValidity, computeAccList, fetchResults } from "../utils/resultUtils.js";

// Check for redirect validity
redirectValidity();

// Add a flag to track if the request is still processing
let isProcessing = ref(true);

// When starting the fetch
sessionStorage.setItem("isProcessing", "true");

// Storage for parsed results
let parsedRes = ref();

// Summary section variables
let resourceTitle = ref("No Title Detected!");
let resourceIdentifier = ref("No Identifier Detected!");
let llmInUse = ref();
let totalFairScore = ref(0.0);
let maxFairScore = ref(0.0);
let totalMetrics = ref();
let showUserAccordions = ref(false);

// Bar Chart section
let fPercent = ref(0.0);
let aPercent = ref(0.0);
let iPercent = ref(0.0);
let rPercent = ref(0.0);
let uPercent = ref(0.0);

let fAccordions;
let aAccordions;
let iAccordions;
let rAccordions;
let userAccordions;

// Function to export results as JSON
const exportToJson = () => {
  const jsonData = JSON.stringify(parsedRes, null, 2);
  const blob = new Blob([jsonData], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "fair-assessment-results.json";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
};

// Cleanup event listener when component unmounts
onUnmounted(() => {
  window.onbeforeunload = null;
  // Clear session storage objects
  sessionStorage.removeItem("formSubmitted");
  sessionStorage.removeItem("initiated_task");
});

// Start looking for results
onMounted(async () => {
  // Add event listener for beforeunload to prevent closing tab before results arrive.
  window.onbeforeunload = (e) => {
    if (isProcessing.value) {
      // Return a message to show in the alert
      return "The request you started is still processing. Are you sure you want to leave?";
    }
  };
  try {
    parsedRes = await fetchResults();
    isProcessing.value = false;
    sessionStorage.setItem("isProcessing", "false");
    sessionStorage.removeItem("formSubmitted");
    sessionStorage.removeItem("initiated_task");
    console.log("Results Received!");

    // get title
    resourceTitle.value = parsedRes["fair_assessment"]["summary"]["title"];
    resourceIdentifier.value = parsedRes["fair_assessment"]["summary"]["identifier"];
    totalMetrics.value = parsedRes["fair_assessment"]["summary"]["total_metrics"];
    llmInUse.value = parsedRes["fair_assessment"]["summary"]["LLM"];

    // get the total fair score
    const _scores = parsedRes["fair_assessment"]["summary"]["score_summary"]["score"];
    Object.keys(_scores).forEach((key) => {
      if (key === "U") {
        // DO Nothing: Don't use the user-defined metrics for final FAIR Score. They are only for user reference
      } else {
        totalFairScore.value += _scores[key];
        maxFairScore.value +=
          parsedRes["fair_assessment"]["summary"]["score_summary"]["score_out_of"][key];
      }
    });
    fPercent.value = (
      parsedRes["fair_assessment"]["summary"]["score_summary"]["score_percent"]["F"] * 100
    ).toFixed(1);
    aPercent.value = (
      parsedRes["fair_assessment"]["summary"]["score_summary"]["score_percent"]["A"] * 100
    ).toFixed(1);
    iPercent.value = (
      parsedRes["fair_assessment"]["summary"]["score_summary"]["score_percent"]["I"] * 100
    ).toFixed(1);
    rPercent.value = (
      parsedRes["fair_assessment"]["summary"]["score_summary"]["score_percent"]["R"] * 100
    ).toFixed(1);

    // Create accordions for individual metrics
    fAccordions = computeAccList(parsedRes["fair_assessment"]["metrics"], "findable");
    aAccordions = computeAccList(parsedRes["fair_assessment"]["metrics"], "accessible");
    iAccordions = computeAccList(parsedRes["fair_assessment"]["metrics"], "interoperable");
    rAccordions = computeAccList(parsedRes["fair_assessment"]["metrics"], "reusable");
    userAccordions = computeAccList(
      parsedRes["fair_assessment"]["metrics"],
      "user-defined-domain-checks"
    );
    if (userAccordions.value.length > 0) {
      showUserAccordions.value = true;
      uPercent.value = (
        parsedRes["fair_assessment"]["summary"]["score_summary"]["score_percent"]["U"] * 100
      ).toFixed(1);
    }
  } catch (error) {
    console.error("An error occurred while processing results. Please try again later");
    console.log(error);
    isProcessing.value = false;
    sessionStorage.setItem("isProcessing", "false");
  }
});
</script>

<template>
  <div>
    <div
      class="container-fluid main-container d-flex justify-content-center align-items-center"
      v-if="isProcessing"
      id="outer"
    >
      <div class="text-center">
        <span class="spinner-border text-primary" role="status" aria-hidden="true"></span>
        <h3 class="mt-3">
          Please wait while your results are being processed...<br />Processing can take between 4-8
          minutes
        </h3>
      </div>
    </div>

    <div class="container-fluid main-container align-content-center" v-if="!isProcessing">
      <h1 class="display-5 text-center">Assessment Results</h1>
      <div
        class="container-fluid d-flex justify-content-center align-items-center my-5"
        id="disclaimer"
      >
        <p>
          <strong>Disclaimer:</strong> LLMs can make mistake. Please double check the answers and if
          there are any major issue, please report them in the feedback section.
        </p>
      </div>

      <div class="container-fluid">
        <h2 class="display-6 text-center">Result Summary</h2>
        <div class="card px-5">
          <div class="card-body justify-content-center">
            <h3 class="card-title d-flex justify-content-center">{{ resourceTitle }}</h3>
            <table class="table my-3">
              <tbody>
                <tr>
                  <th>FAIR Score:</th>
                  <td>{{ totalFairScore }} / {{ maxFairScore }}</td>
                </tr>
                <tr>
                  <th>FAIR Level:</th>
                  <td>{{ ((totalFairScore / maxFairScore) * 100).toFixed(0) }}%</td>
                </tr>
                <tr>
                  <th>Detected Resource PID/URL:</th>
                  <td class="text-break">{{ resourceIdentifier }}</td>
                </tr>
                <tr>
                  <th>Software version:</th>
                  <td>1.0</td>
                </tr>
                <tr>
                  <th>LLM Used:</th>
                  <td>{{ llmInUse }}</td>
                </tr>
                <tr>
                  <th>Total Metrics Measured:</th>
                  <td>{{ totalMetrics }}</td>
                </tr>
                <tr>
                  <th>Export assessment results:</th>
                  <td>
                    <a href="#" @click.prevent="exportToJson">
                      <b>{JSON Export}</b>
                    </a>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="container-fluid my-3 px-4">
            <!-- Findability -->
            <div class="row d-flex my-2">
              <div class="col">
                <strong>Findability:</strong>
              </div>
              <div class="col">
                <div class="progress" style="height: 3em">
                  <div
                    class="progress-bar bg-success"
                    role="progressbar"
                    :style="{ width: fPercent + '%' }"
                    :aria-valuenow="fPercent"
                    aria-valuemin="0"
                    aria-valuemax="100"
                  >
                    {{ fPercent }}%
                  </div>
                </div>
              </div>
              <br />
            </div>
            <!-- Accessibility -->
            <div class="row d-flex my-2">
              <div class="col">
                <strong>Accessbility:</strong>
              </div>
              <div class="col">
                <div class="progress" style="height: 3em">
                  <div
                    class="progress-bar bg-info"
                    role="progressbar"
                    :style="{ width: aPercent + '%' }"
                    :aria-valuenow="aPercent"
                    aria-valuemin="0"
                    aria-valuemax="100"
                  >
                    {{ aPercent }}%
                  </div>
                </div>
              </div>
              <br />
            </div>

            <!-- Interoperability -->
            <div class="row d-flex my-2">
              <div class="col">
                <strong>Interoperability:</strong>
              </div>
              <div class="col">
                <div class="progress" style="height: 3em">
                  <div
                    class="progress-bar bg-warning"
                    role="progressbar"
                    :style="{ width: iPercent + '%' }"
                    :aria-valuenow="iPercent"
                    aria-valuemin="0"
                    aria-valuemax="100"
                  >
                    {{ iPercent }}%
                  </div>
                </div>
              </div>
              <br />
            </div>

            <!-- Reusability -->
            <div class="row d-flex my-2">
              <div class="col">
                <strong>Reusability:</strong>
              </div>
              <div class="col">
                <div class="progress" style="height: 3em">
                  <div
                    class="progress-bar bg-danger"
                    role="progressbar"
                    :style="{ width: rPercent + '%' }"
                    :aria-valuenow="rPercent"
                    aria-valuemin="0"
                    aria-valuemax="100"
                  >
                    {{ rPercent }}%
                  </div>
                </div>
              </div>
              <br />
            </div>

            <!-- User-Defined Metric -->
            <div class="row d-flex my-2" v-if="showUserAccordions">
              <div class="col">
                <strong>User Defined Metrics:</strong>
              </div>
              <div class="col">
                <div class="progress" style="height: 3em">
                  <div
                    class="progress-bar bg-secondary"
                    role="progressbar"
                    :style="{ width: uPercent + '%' }"
                    :aria-valuenow="uPercent"
                    aria-valuemin="0"
                    aria-valuemax="100"
                  >
                    {{ uPercent }}%
                  </div>
                </div>
              </div>
              <br />
            </div>
          </div>
        </div>
      </div>
      <br />
      <br />

      <div class="container-fluid">
        <h2 class="display-6 text-center">Detailed Analysis</h2>
        <div
          class="container-fluid my-3 d-flex justify-content-center align-items-center"
          id="disclaimer2"
        >
          <p>
            The Domain Agnostic Metrics are based on
            <a
              class="link-primary"
              href="https://www.fairsfair.eu/fairsfair-data-object-assessment-metrics-request-comments"
              >FAIRsFAIR Data Object Assessment Metrics (v0.4)</a
            >
          </p>
        </div>

        <!-- Findable Section -->
        <div class="container d-flex justify-content-center">
          <div>
            <h3 class="display-7 text-center">Findable</h3>
            <div>
              <Accordion v-for="(accord, index) in fAccordions" :key="index" :acc="accord" />
            </div>
          </div>
        </div>
        <br />

        <!-- Accessible Section -->
        <div class="container d-flex justify-content-center">
          <div>
            <h3 class="display-7 text-center">Accessible</h3>
            <div>
              <Accordion v-for="(accord, index) in aAccordions" :key="index" :acc="accord" />
            </div>
          </div>
        </div>
        <br />

        <!-- Interoperable Section -->
        <div class="container d-flex justify-content-center">
          <div>
            <h3 class="display-7 text-center">Interoperable</h3>
            <div>
              <Accordion v-for="(accord, index) in iAccordions" :key="index" :acc="accord" />
            </div>
          </div>
        </div>
        <br />

        <!-- Reusable Section -->
        <div class="container d-flex justify-content-center">
          <div>
            <h3 class="display-7 text-center">Reusable</h3>
            <div>
              <Accordion v-for="(accord, index) in rAccordions" :key="index" :acc="accord" />
            </div>
          </div>
        </div>
        <br />

        <div class="container d-flex justify-content-center" v-if="showUserAccordions">
          <div>
            <h3 class="display-7 text-center">User Defined Tests</h3>
            <div>
              <Accordion v-for="(accord, index) in userAccordions" :key="index" :acc="accord" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-container h1 {
  font-size: 3em;
}

.main-container h3 {
  font-size: 1.7em;
}

.spinner-border {
  animation-duration: 1.5s;
  width: 4rem;
  height: 4rem;
}

#disclaimer {
  background-color: #f5dda6;
  min-height: 2em;
  max-height: 6em;
  max-width: 85em;
}

#disclaimer p {
  font-size: 1.6em;
  padding: 2.2em;
}

#disclaimer2 {
  max-height: 4em;
  max-width: 75em;
}

#disclaimer2 p {
  font-size: 1.5em;
  padding: 2.3em;
}
</style>
