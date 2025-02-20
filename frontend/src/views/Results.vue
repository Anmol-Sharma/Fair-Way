<script setup>
import Accordion from "../components/Accordion.vue";
import { onMounted, onUnmounted } from "vue";
import { ref } from "vue";
import { redirectValidity, compute_acc_list, fetchResults } from "../utils/result_utils.js";

// Check for redirect validity
redirectValidity();

// Add a flag to track if the request is still processing
let isProcessing = ref(true);
// When starting the fetch
sessionStorage.setItem("isProcessing", "true");

// Storage for parsed results
let parsed_res = ref();

// Summary section variables
let resource_title = ref("No Title Detected!");
let total_fair_score = ref(0.0);
let max_fair_score = ref(0.0);
let total_metrics = ref();

// Bar Chart section
let f_percent = ref(0.0);
let a_percent = ref(0.0);
let i_percent = ref(0.0);
let r_percent = ref(0.0);

let f_accordions;
let a_accordions;
let i_accordions;
let r_accordions;

// Function to export results as JSON
const exportToJson = () => {
  const jsonData = JSON.stringify(parsed_res, null, 2);
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
    parsed_res = await fetchResults();
    isProcessing.value = false;
    sessionStorage.setItem("isProcessing", "false");
    sessionStorage.removeItem("formSubmitted");
    sessionStorage.removeItem("initiated_task");
    console.log("Results Received!");

    // get title
    resource_title.value = parsed_res["fair_assessment"]["summary"]["title"];
    total_metrics.value = parsed_res["fair_assessment"]["summary"]["total_metrics"];

    // get the total fair score
    const _scores = parsed_res["fair_assessment"]["summary"]["score_summary"]["score"];
    Object.keys(_scores).forEach((key) => {
      total_fair_score.value += _scores[key];
      max_fair_score.value +=
        parsed_res["fair_assessment"]["summary"]["score_summary"]["score_out_of"][key];
    });
    f_percent.value = (
      parsed_res["fair_assessment"]["summary"]["score_summary"]["score_percent"]["F"] * 100
    ).toFixed(1);
    a_percent.value = (
      parsed_res["fair_assessment"]["summary"]["score_summary"]["score_percent"]["A"] * 100
    ).toFixed(1);
    i_percent.value = (
      parsed_res["fair_assessment"]["summary"]["score_summary"]["score_percent"]["I"] * 100
    ).toFixed(1);
    r_percent.value = (
      parsed_res["fair_assessment"]["summary"]["score_summary"]["score_percent"]["R"] * 100
    ).toFixed(1);
    // Create accordions for individual metrics
    f_accordions = compute_acc_list(parsed_res["fair_assessment"]["metrics"], "findable");
    a_accordions = compute_acc_list(parsed_res["fair_assessment"]["metrics"], "accessible");
    i_accordions = compute_acc_list(parsed_res["fair_assessment"]["metrics"], "interoperable");
    r_accordions = compute_acc_list(parsed_res["fair_assessment"]["metrics"], "reusable");
  } catch (error) {
    console.error("An error occurred while fetching results. Please try again later");
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
        <h3 class="mt-3">Please wait while your results are being processed...</h3>
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
            <h3 class="card-title d-flex justify-content-center">{{ resource_title }}</h3>
            <table class="table my-3">
              <tbody>
                <tr>
                  <th>FAIR Score:</th>
                  <td>{{ total_fair_score }} / {{ max_fair_score }}</td>
                </tr>
                <tr>
                  <th>FAIR Level:</th>
                  <td>{{ ((total_fair_score / max_fair_score) * 100).toFixed(0) }}%</td>
                </tr>
                <tr>
                  <th>Detected Resource PID/URL:</th>
                  <td class="text-break">(TODO: Modify Logic)</td>
                </tr>
                <tr>
                  <th>Software version:</th>
                  <td>1.0</td>
                </tr>
                <tr>
                  <th>Total Metrics Measured:</th>
                  <td>{{ total_metrics }}</td>
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
                <div class="progress" style="height: 2.5em">
                  <div
                    class="progress-bar bg-success"
                    role="progressbar"
                    :style="{ width: f_percent + '%' }"
                    :aria-valuenow="f_percent"
                    aria-valuemin="0"
                    aria-valuemax="100"
                  >
                    {{ f_percent }}%
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
                <div class="progress" style="height: 2.5em">
                  <div
                    class="progress-bar bg-info"
                    role="progressbar"
                    :style="{ width: a_percent + '%' }"
                    :aria-valuenow="a_percent"
                    aria-valuemin="0"
                    aria-valuemax="100"
                  >
                    {{ a_percent }}%
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
                <div class="progress" style="height: 2.5em">
                  <div
                    class="progress-bar bg-warning"
                    role="progressbar"
                    :style="{ width: i_percent + '%' }"
                    :aria-valuenow="i_percent"
                    aria-valuemin="0"
                    aria-valuemax="100"
                  >
                    {{ i_percent }}%
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
                <div class="progress" style="height: 2.5em">
                  <div
                    class="progress-bar"
                    role="progressbar"
                    :style="{ width: r_percent + '%' }"
                    :aria-valuenow="r_percent"
                    aria-valuemin="0"
                    aria-valuemax="100"
                  >
                    {{ r_percent }}%
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
            The Following Metrics are based on
            <a
              class="link-primary"
              href="https://www.fairsfair.eu/fairsfair-data-object-assessment-metrics-request-comments"
              >FAIRsFAIR Data Object Assessment Metrics</a
            >
          </p>
        </div>

        <!-- Findable Section -->
        <div class="container d-flex justify-content-center">
          <div>
            <h3 class="display-7 text-center">Findable</h3>
            <div>
              <Accordion v-for="(accord, index) in f_accordions" :key="index" :acc="accord" />
            </div>
          </div>
        </div>
        <br />

        <!-- Accessible Section -->
        <div class="container d-flex justify-content-center">
          <div>
            <h3 class="display-7 text-center">Accessible</h3>
            <div>
              <Accordion v-for="(accord, index) in a_accordions" :key="index" :acc="accord" />
            </div>
          </div>
        </div>
        <br />

        <!-- Interoperable Section -->
        <div class="container d-flex justify-content-center">
          <div>
            <h3 class="display-7 text-center">Interoperable</h3>
            <div>
              <Accordion v-for="(accord, index) in i_accordions" :key="index" :acc="accord" />
            </div>
          </div>
        </div>
        <br />

        <!-- Reusable Section -->
        <div class="container d-flex justify-content-center">
          <div>
            <h3 class="display-7 text-center">Reusable</h3>
            <div>
              <Accordion v-for="(accord, index) in r_accordions" :key="index" :acc="accord" />
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
