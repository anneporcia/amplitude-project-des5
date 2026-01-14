import boto3
from dotenv import load_dotenv
import os

load_dotenv()

access_key = os.getenv('AWS_ACCESS_KEY')
secret_access_key = os.getenv('AWS_SECRET_KEY')
bucket = os.getenv('BUCKET_NAME')

def load_function(data_dir, access_key, secret_access_key, bucket):
    '''
    Docstring for load_function
    
    :param data_dir: local directory data is saved in
    :param access_key: access key
    :param secret_access_key: secret key
    :param bucket: Bucket data is being loaded into
    :param logger: --
    '''
    # Create an S3 Client using AWS Credentials
    s3_client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key
    )

    # session = boto3.Session(profile_name = 'default')

    # s3 = session.client('s3')

    bucketpath = 'python-import'


    # Upload file (Key) to S3 Bucket

    json_files = [f for f in os.listdir(data_dir) if f.endswith('.json')]

    if json_files:
        print(f"Found {len(json_files)} files. Starting upload...")
    # for loop to go through all the files in the data folder
        for file in os.listdir(data_dir):
                # only uploading .json files
                if not file.endswith('.json'):
                        continue
                
                # creates full filepath for .upload_file function
                full_local_path = os.path.join(data_dir, file)
                key = (f'{bucketpath}/{file}')
                
                try:
                    #uploads file from local directory to bucket
                    s3_client.upload_file(full_local_path, bucket, key)
                    # removes the file from local directory
                    os.remove(full_local_path)

                except Exception as e:
                    print(f'Upload error for {file}: {e}')

    else:
        # This runs if json_files is empty
        print('No JSON files found in the directory. Nothing to upload. (┬┬﹏┬┬)')
    
load_function('json_data', access_key, secret_access_key, bucket)
