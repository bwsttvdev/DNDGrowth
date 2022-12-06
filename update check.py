# Import the necessary modules
import requests
import json

# Set the URL of the GitHub repository to check
repo_url = "https://api.github.com/repos/<user>/<repo>"

# Make a GET request to the GitHub API to retrieve information about the repository
response = requests.get(repo_url)

# Parse the response as JSON
repo_info = json.loads(response.text)

# Get the version number of the latest release from the repository info
latest_version = repo_info["latest_release"]["tag_name"]

# Compare the version number of the latest release to the version number of the current version
if latest_version > current_version:
    # If the version number of the latest release is higher, print a message in red text
    print("\033[91m" + "New version available: " + latest_version + "\033[0m")
else:
    # If the version number of the latest release is the same or lower, print a message in green text
    print("\033[92m" + "Up to date" + "\033[0m")
