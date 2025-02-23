async function handlePost(response) {
  // Check for HTTP 500 error
  if (response.status === 500) {
    return { success: false, code: "500", error: "Server Error" };
  }

  if (response.status !== 202) {
    return { success: false, code: response.status.toString(), error: "Data not accepted" };
  }

  // Read JSON response from server
  const jsonResponse = await response.json();
  if (jsonResponse.error === 1) {
    return { success: false, code: response.status.toString(), error: "JSON Parsing Error" };
  }
  return { sucess: true, response: jsonResponse };
}

export async function postData(data, endpoint, headerObj = null) {
  // Initialize request configuration with default method and body
  const req = { method: "POST", body: data };
  // Add headers if provided
  if (headerObj) {
    req.headers = headerObj;
  }

  // Upload the file to backend system for processing
  const response = await fetch(endpoint, req);
  return await handlePost(response);
}
