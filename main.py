import requests
from datetime import datetime

# Configuration
USERNAME = "jalalseidi"
TOKEN = "12345654321"
GRAPH_ID = "graph1"

# Base endpoint
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# Headers for authentication
HEADERS = {"X-USER-TOKEN": TOKEN}

# Date for pixel operations
today = datetime.now().strftime("%Y%m%d")

# Endpoints
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{today}"

# Graph configuration
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}

# Validate user input for commits
while True:
    try:
        commit_count = int(input("How many times did you commit today? "))
        if commit_count < 0:
            raise ValueError("Commit count cannot be negative.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a positive integer.")

# Pixel configuration
pixel_config = {
    "date": today,
    "quantity": str(commit_count),
}

# Update pixel configuration
pixel_update_config = {"quantity": "3"}

# Function to make API requests safely
def make_request(method, url, data=None):
    try:
        if method == "POST":
            response = requests.post(url, json=data, headers=HEADERS)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=HEADERS)
        elif method == "DELETE":
            response = requests.delete(url, headers=HEADERS)
        else:
            return None

        if response.status_code in [200, 201]:
            print(f"Success: {method} request completed.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
        return response
    except requests.RequestException as e:
        print(f"Request failed: {e}")

# Uncomment below to execute API actions
# make_request("POST", GRAPH_ENDPOINT, graph_config)  # Create a graph
# make_request("POST", PIXEL_ENDPOINT, pixel_config)  # Create a pixel
# make_request("PUT", PIXEL_ENDPOINT, pixel_update_config)  # Update a pixel
make_request("DELETE", PIXEL_ENDPOINT)  # Delete a pixel
