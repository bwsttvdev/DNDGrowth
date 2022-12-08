import requests
import os
import re
import json

# GitHub repository where the script is stored
OWNER = "username"
REPO = "my_repo"

# Name and path of the script
SCRIPT_NAME = "my_script.py"
SCRIPT_PATH = "./my_script.py"

# URL of the latest release in the repository
LATEST_RELEASE_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"

# Check for the latest release in the repository
response = requests.get(LATEST_RELEASE_URL)
latest_release = json.loads(response.text)

# Download the script from the latest release
script_url = latest_release["assets"][0]["browser_download_url"]
response = requests.get(script_url)

# Save the script to the local machine
with open(SCRIPT_PATH, "w") as f:
    f.write(response.text)

# Compare the local version of the script with the latest version
local_script = open(SCRIPT_PATH, "r").read()
latest_script = response.text
if local_script != latest_script:
    # Check for new import dependencies in the updated script
    local_imports = set(re.findall(r"import (\w+)", local_script))
    latest_imports = set(re.findall(r"import (\w+)", latest_script))
    new_imports = latest_imports - local_imports
    if new_imports:
        # Install the new import dependencies
        for module in new_imports:
            os.system(f"pip install {module}")

    # Apply the changes to the local version of the script
    with open(SCRIPT_PATH, "w") as f:
        f.write(latest_script)

# Save the updated script and close the program
os.chmod(SCRIPT_PATH, 0o755)
