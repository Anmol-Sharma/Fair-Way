// MODULE TO LOAD THE Global Configurations and make them accessible throughout the package.
import global_config from "../../../configs/global_config.json"

// merge the global and frontend configurations
export const getConfig = () => {
	return {
		global: global_config,
	}
}