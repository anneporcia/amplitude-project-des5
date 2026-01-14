import requests
from dotenv import load_dotenv
import os
from zipfile import ZipFile
from datetime import datetime, timedelta
import logging
import boto3
from dotenv import load_dotenv
import os

from amplitude.amplitude_api_script import api_call
from amplitude.amplitude_api_script import unzip
from logging import logging_function
from amplitude_load_script import load_function

load_dotenv()

aws_access_key_id = os.getenv('AWS_ACCESS_KEY')
aws_secret_access_key = os.getenv('AWS_SECRET_KEY')
bucket = os.getenv('AWS_BUCKET_NAME')

data_dir = 'data'
filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
data_filepath = f'{data_dir}/{filename}.zip'
log_dir = 'logs'


url = 'https://analytics.eu.amplitude.com/api/2/export'

api_logger = logging_function('api',)

api_call(url, data_dir, filename, data_filepath)




