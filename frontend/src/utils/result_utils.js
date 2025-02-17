import router from '../router';
import { ref } from 'vue';
import { FileSizeCheck, sleep } from './helper_utils';

export function redirectValidity(){
    // Check for validity of form submission
    const isFormSubmitted=sessionStorage.getItem("formSubmitted");
    if(isFormSubmitted===null || !isFormSubmitted){
        router.push({name:"Assess"});
    }else{
        let initiated_task=sessionStorage.getItem("initiated_task")
        if(initiated_task===null){
            router.push({name:"Assess"});
            throw new Error("Results not present");
        }
        initiated_task=JSON.parse(initiated_task);
        console.log("Initiated Task:")
        console.log(initiated_task);
    }
}

export function compute_acc_list(test_results, principle){
    /*
        Helper function to build accordions from the test results for all metrics for a given principle.
    */
    let accList = [];

    // Helper function to convert keys to IDs
    // TODO: (low priority) better processing after checking out ids
    const renameMetricID = (key) => {
        if (key === "FsF_R1_1_01M") {
            return "FsF-R1.1-01M";
        }
        return key.replace(/_/g, '-');
    };

    // Helper function to process test results
    const processTestResults = (testResults) => {
      const bodyContent = {};
      for (const [testKey, result] of Object.entries(testResults)) {
          const testId = testKey.replace(/_/g, '-');
          // Special case handling
          if (testKey === "FsF_R1_1_01M-1") {
              bodyContent["FsF-R1.1-01M-1"] = {
                  result: result.result,
                  score: result.score,
                  out_of: result.out_of
              };
          } else {
              bodyContent[testId] = {
                  result: result.result,
                  score: result.score,
                  out_of: result.out_of
              };
          }
      }
      return bodyContent;
  };

    for (const [key, val] of Object.entries(test_results)) {
      if (val.principle === principle) {
          const acId = renameMetricID(key);
          const bodyContent = processTestResults(val.test_results);

          // Determine color based on test results
          let allPassed = true;
          let anyPassed = false;

          for (const test of Object.values(val.test_results)) {
              if (test.score < test.out_of){
                allPassed = false;
                continue
              }
              else if (test.score > 0){
                anyPassed = true;
              }
          }

          let color;
          if (allPassed) {
            color = '#5ac481';
          } else if (!allPassed && anyPassed) {
            color = '#bdb359';
          } else {
            color = '#c95564';
          }

          accList.push({
              title: `${acId}: ${val.metric_name}`,
              id: acId,
              test_analysis: bodyContent,
              color: color
          });
      }
  }

  return ref(accList);
}

export async function postData(data, endpoint, headerObj = null) {
  // Initialize request configuration with default method and body
  const req = { method: 'POST', body: data };
  // Add headers if provided
  if (headerObj) {
      req.headers = headerObj;
  }

  try {
      // Upload the file to backend system for processing
      const response = await fetch(endpoint, req);

      // Check for HTTP 500 error
      if (response.status === 500) {
          router.push({ name: '500' });
          throw new Error('Internal Server Error');
      }

      if (response.status !== 202) {
          throw new Error(`HTTP response code ${response.status}. Data has not been accepted.`);
      }

      // Read JSON response from server
      const jsonResponse = await response.json();
      if (jsonResponse.error === 1) {
          throw new Error(jsonResponse.message);
      }

      sessionStorage.setItem('formSubmitted', 'true');
      sessionStorage.setItem('initiated_task', JSON.stringify(jsonResponse));

  } catch (error) {
      console.error('Error in postData:', error);
      throw error; // Re-throw the error after logging it
  }
}

export async function online_assessment(url){
    // Upload the file to backend system for processing
    try {
      const _data = { url: url };
      const h = { "Content-Type": "application/json" };
      await postData(JSON.stringify(_data), "/api/OnlineAnalyze", h);
      router.push({ name: 'Results' });
    } catch (error) {
      console.error('Error in online_assessment:', error);
      // If it's a 500, already redirected in postData
    }
}

async function validateAndProcess(meta_file) {
    // FOR XML and JSON FILES
    const fileContent = await meta_file.text();
    let parsedContent;
    let cleanedContent;

    if (meta_file.type === "text/xml" ||
        meta_file.type === "application/xml" ||
        meta_file.type === "application/xhtml+xml") {
        try {
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(fileContent, "text/xml");

            // Check for parsing errors
            const parserError = xmlDoc.querySelector('parsererror');
            if (parserError) {
                throw new Error("Invalid XML format");
            }

            parsedContent = xmlDoc;

            // Clean the XML content
            const serializer = new XMLSerializer();
            cleanedContent = serializer.serializeToString(parsedContent)
                .replace(/>\s+</g, '><') // Remove whitespace between tags
                .trim(); // Remove leading and trailing whitespace

        } catch (e) {
            alert("Invalid XML file");
            throw new Error("Invalid XML file: " + e.message);
        }
    }
    else if (meta_file.type === "application/json" ||
             meta_file.type === "application/ld+json") {
        try {
            parsedContent = JSON.parse(fileContent);

            // Clean the JSON content
            cleanedContent = JSON.stringify(parsedContent, null, 0); // Remove all whitespace

        } catch (e) {
            alert("Invalid JSON file");
            throw new Error("Invalid JSON file: " + e.message);
        }
    }

    // Create a new File object with cleaned content
    const fileName = meta_file.name;
    const fileType = meta_file.type;
    const blob = new Blob([cleanedContent], { type: fileType });

    return new File([blob], fileName, { type: fileType });
}


export async function offline_assessment(event, Files, metadata_file){
	// Get the file information
	try {
    let meta_file = Files[metadata_file];
    let valid_file_size = FileSizeCheck(meta_file);
    if (!valid_file_size) {
        alert("File Size Too Big");
        return;
    }

    if (meta_file.type === "text/xml" ||
        meta_file.type === "application/xml" ||
        meta_file.type === "application/xhtml+xml" ||
        meta_file.type === "application/json" ||
        meta_file.type === "application/ld+json"
    ){
        meta_file = await validateAndProcess(meta_file)
    }

    const formData = new FormData();
    formData.append('file', meta_file);
    await postData(formData, "/api/OfflineAnalyze");
    router.push({ name: 'Results' });

} catch (error) {
    console.error('Error in offline_assessment:', error);
    if (error.message.includes('500')) {
        router.push({ name: 'InternalServerError' });
    } else {
        alert(error.message);
    }
}
}

// ####################################
// Utility functions for connections
// ####################################

export async function fetchResults() {
  try {
        const initiatedTask = sessionStorage.getItem("initiated_task");
        if (!initiatedTask) {
            throw new Error('No initiated task found in sessionStorage');
        }
        const initiated_task = JSON.parse(initiatedTask);
        let delay = 30000; // Start with 30 seconds

        while (true) {
            const statusResponse = await fetch(`/api/Status/${initiated_task.task_id}`, {});

            // Check for HTTP 500 error
            if (statusResponse.status === 500) {
                router.push({ name: '500' });
                throw new Error('Internal Server Error');
            }

            const status = await statusResponse.json();

            if (status.success) {
                const resultsResponse = await fetch(`/api/Results/${initiated_task.task_id}`, {});

                // Check for HTTP 500 error
                if (resultsResponse.status === 500) {
                    router.push({ name: '500' });
                    throw new Error('Internal Server Error');
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
                delay = Math.max(delay / 2, 5000);
                await sleep(delay);
            }
        }
  } catch (error) {
        console.error("Error fetching results:", error);
        throw error;
  }
}