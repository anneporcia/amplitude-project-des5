# Amplitude Project

## **Extract Script**

* **Automated Date Handling**: Automatically targets data from 3 days ago—no manual date entry required.
* **Professional Logging**: Creates a `/logs` directory and tracks every step (successes, status codes, and errors) with timestamps.
* **Deep Extraction**: Unpacks the primary Amplitude `.zip` and automatically decompresses nested `.gz` files into clean, readable JSON.
* **Temporary Workspace**: Uses system temporary directories for extraction to keep your project folder clutter-free.

---

## 🛠 Setup and Usage

Follow these steps to get the extraction pipeline running:

### 1. Installation and Requirements
Ensure you have Python 3.x installed. This script uses the `requests` and `python-dotenv` libraries.
pip install requests python-dotenv

### 2. Configure Credentials

Create a `.env` file in the root directory to store your keys safely:

AMP_API_KEY=your_amplitude_api_key
AMP_SECRET_KEY=your_amplitude_secret_key

### 3. Usage & Execution

Simply run the script. It will automatically calculate the date, ping the Amplitude EU server, and process the files:

python your_script_name.py

---

## 📂 Project Structure

The script manages three distinct folders to organize your data lifecycle:
- **.env**                # Your private API keys
- **script.py**           # The main extraction logic
- **logs/**               # Log files (e.g., amplitude_extract_20260109.log)
- **data/**               # The raw .zip files downloaded from the API
- **json_data/**          # Final processed JSON files ready for analysis


---

## ⚙️ Technical Workflow

1. **Logging Init**: Creates a `/logs` folder and starts a new log file for the session.
2. **API Call**: Connects to `analytics.eu.amplitude.com` using Basic Auth.
3. **Download**: Saves the raw payload into the `/data` folder with a timestamped filename.
4. **Decompression**:
   * Unzips the main archive to a temporary folder.
   * Identifies the internal folder structure.
   * Walks through the directories to find `.gz` files.
   * Decompresses JSON data into the `/json_data` folder.


5. **Cleanup**: Automatically deletes the temporary extraction workspace.

---

## 📝 Important Notes

* **Time Module**: Ensure `import time` is added to your script to support the `time.sleep(10)` function in your retry loop.
* **Data Residency**: Currently set to the **EU Server**. For US-based projects, update the URL to `https://amplitude.com/api/2/export`.
* **Git Best Practices**: If pushing to a public repo, ensure your `.gitignore` includes `.env`, `data/`, `json_data/`, and `logs/`.


