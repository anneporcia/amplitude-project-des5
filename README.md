# Amplitude Extract Script

Python designed to automate the retrieval of raw event data from the **Amplitude Export API**. This script handles authentication, manages local directory structures, and includes a retry mechanism for resilient data fetching.

---

## 🚀 Features

* **Automated Exports**: Downloads raw event data for a specified date range.
* **Environment Security**: Integration with `python-dotenv` to keep API credentials out of your source code.
* **Automated Directory Management**: Checks for and creates a `/data` directory if it doesn't exist.
* **Retry Logic**: Includes a loop to handle transient server errors (5xx) automatically.
* **Timestamped Files**: Saves exports as `.zip` files named by the exact download time for easy versioning.

---

## 🛠 Setup and Usage

To get this script running, follow these steps in order:

1. **Install Dependencies**:
   Open your terminal and run:
   pip install requests python-dotenv


2. **Configure Environment Variables**:
  Create a file named `.env` in the same folder as your script and add your Amplitude API credentials:
  AMP_API_KEY=your_amplitude_api_key
  AMP_SECRET_KEY=your_amplitude_secret_key


3. **Set Your Date Range**:
Inside the script, modify the `dates` dictionary to match the time period you want to export (Format: `YYYYMMDDTHH`):
dates = {
    'start': '20260101T00',
    'end': '20260108T00'
}


4. **Verify Imports**:
Ensure your script includes `import time` at the top to support the retry delay functionality.


6. **Execute the Script**:
Run the following command in your terminal:
python your_script_name.py


## 📂 Project Structure

After a successful run, your project folder will look like this:
 .env                # Your private API keys (do not share!)
 your_script.py      # The export script
 data/               # Created automatically by the script

---

## 📝 Important Notes

* **Data Residency**: This script uses the **EU residency server** (`analytics.eu.amplitude.com`). If your project is hosted in the US, update the `url` variable to: `https://amplitude.com/api/2/export`.
* **Security**: Add `.env` to your `.gitignore` file to ensure your API Secret Key is never uploaded to a public GitHub repository.
