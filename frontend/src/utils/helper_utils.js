import { getConfig } from "./config_loader.js"
const config = getConfig();

export function FileSizeCheck(meta_file){
    const maxFileSize = config.global["max_metadata_file_size"]
    if (meta_file.size > maxFileSize) {
        return false; // File exceeds the maximum size
    } else {
        return true;  // File is within the allowed size limit
    }
}

// Define a sleep function to perform sleep operations
export function sleep(ms) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}