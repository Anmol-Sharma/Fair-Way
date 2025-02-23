import { getConfig } from "./config_loader.js";
const config = getConfig();

export function fileSizeCheck(meta_file) {
  const maxFileSize = config.global["max_metadata_file_size"];
  if (meta_file.size > maxFileSize) {
    return false; // File exceeds the maximum size
  } else {
    return true; // File is within the allowed size limit
  }
}

// Define a sleep function to perform sleep operations
export function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * Validates vocabulary data in CSV format
 * @param {string} vocabData - Raw CSV string with vocabulary and descriptions
 * @returns {Object} Validation result with status and any error messages
 */
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
    result.errors.push("No valid data lines found");
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
