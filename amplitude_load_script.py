import boto3
from dotenv import load_dotenv
import os

load_dotenv()

aws_access_key_id = os.getenv('AWS_ACCESS_KEY')
aws_secret_access_key = os.getenv('AWS_SECRET_KEY')
bucket = os.getenv('AWS_BUCKET_NAME')

# Create an S3 Client using AWS Credentials
# s3_client = boto3.client(
#     's3',
#     aws_access_key_id=aws_access_key_id,
#     aws_secret_access_key=aws_secret_access_key
# )

session = boto3.Session(profile_name = 'default')

s3 = session.client('s3')

filepath = 'json_data'
keypath = 'python-import'


# Upload file (Key) to S3 Bucket

json_files = [f for f in os.listdir(filepath) if f.endswith('.json')]

if json_files:
    print(f"Found {len(json_files)} files. Starting upload...")
# for loop to go through all the files in the data folder
    for file in os.listdir(filepath):
            # only uploading .json files
            if not file.endswith('.json'):
                    continue
            
            # creates full filepath for .upload_file function
            full_local_path = os.path.join(filepath, file)
            key = os.path.join(keypath, file)
            
            try:
                #uploads file from local directory to bucket
                s3.upload_file(full_local_path, bucket, key)
                # removes the file from local directory
                os.remove(full_local_path)

            except Exception as e:
                print(f'Upload error for {file}: {e}')

else:
    # This runs if json_files is empty
    print('No JSON files found in the directory. Nothing to upload. (┬┬﹏┬┬)')