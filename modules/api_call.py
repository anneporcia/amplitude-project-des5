# imported libaries for api call and logging
import requests
from dotenv import load_dotenv
import os
from zipfile import ZipFile
from datetime import datetime, timedelta
import logging
import time

def api_call(url, folder, filename, input_dir, logger):
    load_dotenv()

    yesterday = datetime.now() - timedelta(days=1)

    dates = {
        'start': yesterday.strftime('%Y%m%dT00'),
        'end': yesterday.strftime('%Y%m%dT23')
    }

    api_key = os.getenv('AMP_API_KEY')
    secret_key = os.getenv('AMP_SECRET_KEY')

    number_of_tries = 3
    count = 0

    while count < number_of_tries:

        response = requests.get(url, params=dates,auth=(api_key, secret_key), timeout=20)

        rsc = response.status_code
        logger.info(f"API Call Response Code: '{rsc}'")
        logger.info("Data retrieved successfully.")

        if rsc == 200:
            
            if os.path.exists(folder):
                pass
            else:
                os.mkdir(folder)

            try:
                logger.info("Saving data to data.zip")
                with open(input_dir, 'wb') as f:
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
