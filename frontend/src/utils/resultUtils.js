import router from "../router";
import { ref } from "vue";

// ###########################################################
// #        Define Helper Functions for internal Use         #
// ###########################################################
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function renameId(id) {
  // Helper function to convert python module name syntax Metric/ Test Ids to their actual values
  const matches = id.match(/[A-Za-z]\d_\d/g);
  if (matches && matches.length > 0) {
    const patternMatch = matches[0];
    id = id.replace(patternMatch, patternMatch.replace("_", "."));
  }
  return id.replace(/_/g, "-");
}

// Helper function to process test results and generate Body content for each test.
function processTestResults(testResults) {
  const bodyContent = {};
  for (const [testKey, result] of Object.entries(testResults)) {
    const testId = renameId(testKey);
    bodyContent[testId] = {
      result: result.result,
      score: result.score,
      out_of: result.out_of,
    };
  }
  return bodyContent;
}

function determineColor(testResults) {
  // Determine color based on test results
  let allPassed = true;
  let anyPassed = false;

  for (const test of Object.values(testResults)) {
    if (test.score > 0) {
      anyPassed = true;
    }
    if (test.score < test.out_of) {
      allPassed = false;
      continue;
    }
  }

  let color;
  if (allPassed) {
    // All tests passed --> Green
    color = "#5ac481";
  } else if (!allPassed && anyPassed) {
    // Some tests passed --> Yello
    color = "#bdb359";
  } else {
    // No tests passed --> Red
    color = "#c95564";
  }
  return color;
}
// ###############################################################################

// ###########################################################
// #        Define Helper Functions for external Use         #
// ###########################################################

export function redirectValidity() {
  // Check for validity of form submission
  const isFormSubmitted = sessionStorage.getItem("formSubmitted");
  if (isFormSubmitted === null || !isFormSubmitted) {
    router.push({ name: "Assess" });
  } else {
    let initiatedTask = sessionStorage.getItem("initiated_task");
    if (initiatedTask === null) {
      console.log("No request found, redirecting to Assessment page.");
      router.push({ name: "Assess" });
    }
    initiatedTask = JSON.parse(initiatedTask);
    console.log("Initiated Task:", initiatedTask);
  }
}

export function computeAccList(testResults, principle) {
  /*
    Helper function to build accordions from the test results for all metrics for a given principle.
  */
  let accList = [];

  for (const [key, val] of Object.entries(testResults)) {
    // Process FsF Metrics
    if (principle != "user" && val.principle === principle) {
      const acId = renameId(key);
      const bodyContent = processTestResults(val.test_results);
      const color = determineColor(val.test_results);
      accList.push({
        title: `${acId}: ${val.metric_name}`,
        id: acId,
        test_analysis: bodyContent,
        color: color,
      });
    } else if (principle === "user" && !("principle" in val)) {
      // Process User Metrics
      const acId = renameId(key);
      const bodyContent = processTestResults(val.test_results);
      const color = determineColor(val.test_results);
      accList.push({
        title: `${acId}: ${val.metric_name}`,
        id: acId,
        test_analysis: bodyContent,
        color: color,
      });
    }
  }
  return ref(accList);
}

export async function fetchResults() {
  try {
    const initiatedTask = sessionStorage.getItem("initiated_task");
    if (!initiatedTask) {
      // Update the throw with actual user notifications
      throw new Error("No initiated task found in sessionStorage");
    }
    const initiated_task = JSON.parse(initiatedTask);
    let delay = 60000; // Start with 60 seconds
    const startTime = Date.now();
    const timeout = 1800000; // 30 minutes in milliseconds

    while (true) {
      const currentTime = Date.now();
      if (currentTime - startTime >= timeout) {
        throw new Error("Timeout exceeded after 30 minutes");
      }
      const statusResponse = await fetch(`/api/Status/${initiated_task.task_id}`, {});

      // Check for HTTP 500 error
      if (statusResponse.status === 500) {
        router.push({ name: "500" });
        throw new Error("Internal Server Error");
      }

      const status = await statusResponse.json();

      if (status.success) {
        const resultsResponse = await fetch(`/api/Results/${initiated_task.task_id}`, {});

        // Check for HTTP 500 error
        if (resultsResponse.status === 500) {
          router.push({ name: "500" });
          throw new Error("Internal Server Error");
        }

        const parsed_results = await resultsResponse.json();

        if (parsed_results.task_id === initiated_task.task_id) {
          return parsed_results;
        } else {
          throw new Error("Task ID doesn't Match");
        }
      } else {
        console.log("Awaiting Results");
        // Update delay for next iteration check for status update
        delay = Math.max(delay / 2, 3000);
        await sleep(delay);
      }
    }
  } catch (error) {
    console.error("Error fetching results:", error);
    throw error;
  }
}

// ###############################################################################
