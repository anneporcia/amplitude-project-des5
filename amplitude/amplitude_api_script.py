# imported libaries for api call and logging
import requests
from dotenv import load_dotenv
import os
from zipfile import ZipFile
from datetime import datetime, timedelta
import logging

# variables for the filenames and directories
dir = 'data'
log_dir = 'logs'
filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filepath = f'{dir}/{filename}.zip'
log_filename = f"{log_dir}/amplitude_extract_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

if os.path.exists(log_dir):
    pass
else:
    os.mkdir(log_dir)

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_filename
)

logger = logging.getLogger()

yesterday = datetime.now() - timedelta(days=3)

def api_call(url):
    load_dotenv()
    dates = {
        'start': yesterday.strftime('%Y%m%dT00'),
        'end': yesterday.strftime('%Y%m%dT23')
    }

    api_key = os.getenv('AMP_API_KEY')
    secret_key = os.getenv('AMP_SECRET_KEY')

    number_of_tries = 3
    count = 0

    while count < number_of_tries:

        response = requests.get(url, params=dates,auth=(api_key, secret_key))

        rsc = response.status_code
        logger.info(f"API Call Response Code: '{rsc}'")
        logger.info("Data retrieved successfully.")

        if rsc == 200:
            
            if os.path.exists(dir):
                pass
            else:
                os.mkdir(dir)

            try:
                logger.info("Saving data to data.zip")
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                # with ZipFile(filepath, 'w') as file:
                #     file.write(filepath)
                    logger.info("Data saved to data.zip")
                
                print(f'Download successful at {filename} (❁´◡`❁)')

            except Exception as e:
                print(f"An error occurred: {e}")
            break

        elif rsc > 499 or rsc < 200:
            print(response.reason)
            logger.error(f"API Call Error '{response.status_code}: {response.reason}'")
            time.sleep(10)
            count += 1

        else:
            print(response.reason)
            logger.error(f"API Call Error '{response.status_code}: {response.reason}'")
            break

api_call('https://analytics.eu.amplitude.com/api/2/export')

import tempfile
import gzip
import shutil

def unzip():

    # Create a temporary directory for extraction
    temp_dir = tempfile.mkdtemp()

    # Create local output directory
    data_dir = "json_data"
    os.makedirs(data_dir, exist_ok=True)

    # unpack the .zip folder to the temp directory
    with ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

    day_folder = next(f for f in os.listdir(temp_dir) if f.isdigit())
    day_path = os.path.join(temp_dir, day_folder)

    for root, _, files in os.walk(day_path):
        for file in files:
            if file.endswith('.gz'):
                # Process each .gz file
                print(file)

            gz_path = os.path.join(root, file)
            json_filename = file[:-3]  
            output_path = os.path.join(data_dir, json_filename)

            with gzip.open(gz_path, 'rb') as gz_file, open(output_path, 'wb') as out_file:
                shutil.copyfileobj(gz_file, out_file)

    shutil.rmtree(temp_dir)

unzip()
