#import functions from modules
from modules.api_call import api_call
from modules.unzip_files import unzip
from modules.load import upload_to_s3
from modules.logger import logging_function

#import necessary packages
import logging
from dotenv import load_dotenv
import os
from datetime import datetime

# define variables needed for the functions
url = 'https://analytics.eu.amplitude.com/api/2/export'
folder = 'data'
filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
input_dir = f'{folder}/{filename}.zip'
output_dir = 'json_data'

load_dotenv()

access_key = os.getenv('AWS_ACCESS_KEY')
secret_access_key = os.getenv('AWS_SECRET_KEY')
bucket = os.getenv('BUCKET_NAME')
bucket_folder = 'python-import'

# logging function saved in variables
api_logger = logging_function('api_call', filename)
unzip_logger = logging_function('unzip', filename)
load_logger = logging_function('load', filename)

# functions carrying out the script
api_call(url, folder, filename, input_dir, api_logger)

unzip(input_dir, output_dir, unzip_logger)

upload_to_s3(output_dir, access_key, secret_access_key, bucket, bucket_folder)