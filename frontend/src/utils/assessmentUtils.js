import { getConfig } from "./config_loader.js";
import { postData } from "./networkUtils.js";

const config = getConfig();

async function validateAndProcess(meta_file) {
  // FOR XML and JSON FILES
  const fileContent = await meta_file.text();
  let parsedContent;
  let cleanedContent;

  if (
    meta_file.type === "text/xml" ||
    meta_file.type === "application/xml" ||
    meta_file.type === "application/xhtml+xml"
  ) {
    try {
      const parser = new DOMParser();
      const xmlDoc = parser.parseFromString(fileContent, "text/xml");

      // Check for parsing errors
      const parserError = xmlDoc.querySelector("parsererror");
      if (parserError) {
        throw new Error("Invalid XML format");
      }

      parsedContent = xmlDoc;

      // Clean the XML content
      const serializer = new XMLSerializer();
      cleanedContent = serializer
        .serializeToString(parsedContent)
        .replace(/>\s+</g, "><") // Remove whitespace between tags
        .trim(); // Remove leading and trailing whitespace
    } catch (e) {
      alert("Invalid XML file");
      throw new Error("Invalid XML file: " + e.message);
    }
  } else if (meta_file.type === "application/json" || meta_file.type === "application/ld+json") {
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

function fileSizeCheck(meta_file) {
  const maxFileSize = config.global["max_metadata_file_size"];
  if (meta_file.size > maxFileSize) {
    return false; // File exceeds the maximum size
  } else {
    return true; // File is within the allowed size limit
  }
}

export function validateVocabulary(vocabData) {
  // Return object structure
  const result = {
    isValid: true,
    errors: [],
    data: [], // Will contain parsed data if valid
  };

  // Split into lines and remove empty lines
  const lines = vocabData
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line.length > 0);

  if (lines.length === 0) {
    result.isValid = false;
    result.errors.push("No valid vocabulary condition defined");
    return result;
  }

  if (lines.length > 1) {
    result.isValid = false;
    result.errors.push(
      "For a single Vocab Test Please define at most one vocabulary item.\nMove additional items to another test."
    );
    return result;
  }

  // Process each line
  lines.forEach((line, index) => {
    // Split by comma and trim each part
    const parts = line.split(",").map((part) => part.trim());

    // Check if line has exactly 2 columns
    if (parts.length !== 2) {
      result.isValid = false;
      result.errors.push(`Line ${index + 1}: Expected 2 columns, found ${parts.length}`);
      return;
    }

    const [vocabulary, description] = parts;

    // Validate vocabulary name
    if (!vocabulary) {
      result.isValid = false;
      result.errors.push(`Line ${index + 1}: Vocabulary name is empty`);
    } else if (vocabulary.length < 2) {
      result.isValid = false;
      result.errors.push(`Line ${index + 1}: Vocabulary name must be at least 2 characters`);
    } else if (vocabulary.length > 75) {
      result.isValid = false;
      result.errors.push(`Line ${index + 1}: Vocabulary name must not exceed 75 characters`);
    }

    // Validate description
    if (!description) {
      result.isValid = false;
      result.errors.push(`Line ${index + 1}: Description is empty`);
    } else if (description.length < 5) {
      result.isValid = false;
      result.errors.push(`Line ${index + 1}: Description must be at least 5 characters`);
    } else if (description.length > 500) {
      result.isValid = false;
      result.errors.push(`Line ${index + 1}: Description must not exceed 500 characters`);
    }

    // Check for duplicate vocabulary names
    const isDuplicate = result.data.some(
      (item) => item.vocabulary.toLowerCase() === vocabulary.toLowerCase()
    );

    if (isDuplicate) {
      result.isValid = false;
      result.errors.push(`Line ${index + 1}: Duplicate vocabulary name "${vocabulary}"`);
    }

    // Store valid data
    if (result.isValid) {
      result.data.push({ vocabulary, description });
    }
  });

  return result;
}

export async function offlineAssessmentRequest(Files, metadataFile, advancedTests) {
  // Get the file information
  let metaFile = Files[metadataFile];
  let validFileSize = fileSizeCheck(metaFile);
  if (!validFileSize) {
    alert("File Size Too Big");
    return;
  }

  if (
    metaFile.type === "text/xml" ||
    metaFile.type === "application/xml" ||
    metaFile.type === "application/xhtml+xml" ||
    metaFile.type === "application/json" ||
    metaFile.type === "application/ld+json"
  ) {
    metaFile = await validateAndProcess(metaFile);
  }

  const formData = new FormData();
  formData.append("file", metaFile);
  formData.append("advancedTests", JSON.stringify(advancedTests));
  return await postData(formData, "/api/OfflineAnalyze");
}

export async function onlineAssessmentRequest(_data) {
  // Upload the file to backend system for processing
  const h = { "Content-Type": "application/json" };
  return await postData(JSON.stringify(_data), "/api/OnlineAnalyze", h);
}
