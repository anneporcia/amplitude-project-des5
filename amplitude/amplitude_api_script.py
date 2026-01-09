import requests
from dotenv import load_dotenv
import os
from zipfile import ZipFile
from datetime import datetime

load_dotenv()

url = 'https://analytics.eu.amplitude.com/api/2/export'

dates = {
    'start': '20260101T00',
    'end': '20260108T00'
}

api_key = os.getenv('AMP_API_KEY')
secret_key = os.getenv('AMP_SECRET_KEY')

number_of_tries = 3
count = 0

while count < number_of_tries:

    response = requests.get(url, params=dates,auth=(api_key, secret_key))

    rsc = response.status_code

    filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    if rsc == 200:
        dir = 'data'
        if os.path.exists(dir):
            pass
        else:
            os.mkdir(dir)

        filepath = f'{dir}/{filename}.zip'

        try:
            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f'Download successful at {filename} (❁´◡`❁)')
        except Exception as e:
            print(f"An error occurred: {e}")
        break

    elif rsc > 499 or rsc < 200:
        print(response.reason)
        time.sleep(10)
        count += 1

    else:
        print(response.reason)
        break
