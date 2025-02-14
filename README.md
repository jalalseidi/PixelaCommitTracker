# Pixela Commit Tracker

This Python script interacts with the [Pixela API](https://pixe.la/) to track daily coding activity by logging the number of Git commits you make. It allows users to:

- Create a graph for tracking commits.
- Add daily commit data (pixels) to the graph.
- Update an existing pixel (commit count).
- Delete a pixel.

## 🚀 Features

- Uses the Pixela API for visual tracking of coding activity.
- Accepts user input for the number of commits made each day.
- Includes error handling for API requests and input validation.
- Supports POST (create), PUT (update), and DELETE (remove) operations.

## 🛠 Setup

### 1️⃣ Prerequisites

- Python 3.x
- `requests` library (install it with `pip install requests`)
- A Pixela account (sign up at [Pixela](https://pixe.la/))

### 2️⃣ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/pixela-commit-tracker.git
   cd pixela-commit-tracker
   ```

2. Install dependencies:

   ```bash
   pip install requests
   ```

3. Update the script with your **Pixela username** and **API token**:

   ```python
   USERNAME = "your_pixela_username"
   TOKEN = "your_secure_token"
   ```

## 🔧 Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. Enter your number of commits when prompted.

3. The script will:
   - Send data to Pixela.
   - Allow updates to existing entries.
   - Delete entries when needed.

## 📌 API Endpoints Used

- **Create a graph**: `POST /v1/users/{username}/graphs`
- **Create a pixel**: `POST /v1/users/{username}/graphs/{graphID}/{date}`
- **Update a pixel**: `PUT /v1/users/{username}/graphs/{graphID}/{date}`
- **Delete a pixel**: `DELETE /v1/users/{username}/graphs/{graphID}/{date}`

## 🎯 Future Enhancements

- Add a function to retrieve and display historical commit data.
- Implement a GUI for easier interaction.
- Automate daily tracking with a scheduler.

## 📜 License

This project is open-source and available under the MIT License.

