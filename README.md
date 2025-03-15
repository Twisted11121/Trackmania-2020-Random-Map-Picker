# Trackmania-2020-Random-Map-Picker
Trackmania 2020 Random Map Picker Python

This script downloads a random map from the Trackmania Exchange website and saves it to a specified directory. The script performs the following steps:

- Sets the user directory where the map will be saved.
- Fetches a random map from the Trackmania Exchange website.
- Extracts the map ID and name from the fetched HTML content.
- Downloads the map file using the extracted map ID.
- Saves the downloaded map file to the specified directory.
- Optionally, opens the downloaded map file.

Requirements
The script requires the following Python packages:
requests
beautifulsoup4

pip install requests beautifulsoup4

Usage:
1. Set the user_directory variable to the directory where you want to save the downloaded maps. Ensure that the slashes are forward slashes (/).
2. Run the script.
