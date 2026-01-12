# Amplitude-to-S3 Data Pipeline

A Python-based pipeline that automates the extraction of raw event data from the **Amplitude Export API**, transforms the nested compressed files into clean JSON, and loads them directly into an **AWS S3 Bucket**.

---

## 🚀 Pipeline Features

* **Automated Extraction**: Fetches data from 3 days ago (Amplitude settled-data window) from the EU residency server.
* **Robust Logging**: Detailed tracking of API status codes, file counts, and upload success/failure in the `/logs` directory.
* **Recursive Decompression**: Unpacks the primary `.zip` and all nested `.gz` files automatically.
* **S3 Integration**: Uploads processed JSON files to a specified AWS S3 prefix (`python-import/`).
* **Auto-Cleanup**: Automatically deletes local JSON files after a successful S3 upload to save disk space.

---

## 🛠 Setup and Usage

### 1. Install Dependencies
You will need the `requests`, `python-dotenv`, and `boto3` (AWS SDK) libraries:
pip install requests python-dotenv boto3


### 2. Configure AWS CLI

The script uses the `default` profile from your AWS credentials file. Ensure you have run:

```
aws configure

```

### 3. Environment Variables

Create a `.env` file in the root directory and provide your credentials:

```env
# Amplitude Credentials
AMP_API_KEY=your_amplitude_api_key
AMP_SECRET_KEY=your_amplitude_secret_key

# AWS Credentials
AWS_BUCKET_NAME=your_s3_bucket_name

```

### 4. Run the Pipeline

Execute the script to start the full flow:

```bash
python your_script_name.py

```

---

## 📂 Project Structure

The script manages the following directory lifecycle:

```text
.
├── .env                # Private credentials
├── extract_script.py   # The full ETL script
├── load_script.py   # The full ETL script
├── logs/               # Execution logs for auditing
├── data/               # Raw .zip archives from Amplitude
└── json_data/          # Temporary folder for extracted JSONs (cleaned after upload)

```

---

## ⚙️ How It Works

### Part 1: Extraction (API)

The script connects to the Amplitude EU Export API. It targets a 24-hour window from three days prior to the current date to ensure data completeness.

### Part 2: Transformation (Unzip/Decompress)

The downloaded file is a `.zip` containing several folders, which in turn contain multiple `.gz` files. The script:

1. Extracts the main `.zip` to a temporary directory.
2. Walks through the subdirectories to find all `.gz` files.
3. Decompresses them into standard `.json` files in the `/json_data` folder.

### Part 3: Loading (AWS S3)

The script identifies all `.json` files in the `/json_data` folder and:

1. Uploads them to `s3://[your-bucket]/python-import/[filename].json`.
2. Upon a successful upload, the local copy of the JSON file is **deleted** to maintain a clean environment.

---

## 📝 Important Notes

* **Error Handling**: If an upload fails, the local file is preserved so you don't lose data.
* **Data Residency**: Currently configured for **Amplitude EU**. For US projects, update the URL to `https://amplitude.com/api/2/export`.
* **Security**: Ensure `logs/`, `data/`, `json_data/`, and `.env` are added to your `.gitignore` to prevent sensitive data from reaching GitHub.

---

