# import necessary packages for uplaoding to s3 and logging
import boto3
import os
from dotenv import load_dotenv
import logging

# defining load to s3 function
def upload_to_s3(output_dir, access_key, secret_access_key, bucket, bucket_folder, logger):

    # Create an S3 Client using AWS Credentials
    s3_client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key
    )

    # alternative for when keys/credentials aren't working
    # session = boto3.Session(profile_name = 'default')
    # s3 = session.client('s3')


    # Upload file (Key) to S3 Bucket

    json_files = [f for f in os.listdir(output_dir) if f.endswith('.json')]

    if json_files:
        print(f"Found {len(json_files)} files. Starting upload...")
    # for loop to go through all the files in the data folder
        for file in os.listdir(output_dir):
                # only uploading .json files
                if not file.endswith('.json'):
                        continue
                
                # creates full filepath for .upload_file function
                full_local_path = os.path.join(output_dir, file)
                key = (f'{bucket_folder}/{file}')
                
                try:
                    #uploads file from local directory to bucket
                    s3_client.upload_file(full_local_path, bucket, key)
                    # removes the file from local directory
                    os.remove(full_local_path)
                    logger.info(f"{file} - Upload successful! (～￣▽￣)～")

                except Exception as e:
                    print(f'Upload error for {file}: {e}')
                    logger.error(f'Upload error for {file}: {e}')

    else:
        # This runs if json_files is empty
        print('No JSON files found in the directory. Nothing to upload. (┬┬﹏┬┬)')
        logger.info("No JSON files found in the directory. Nothing to upload. (┬┬﹏┬┬)")