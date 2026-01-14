import tempfile
import gzip
import shutil
from zipfile import ZipFile
import os
import logging

def unzip(input_dir, output_dir, logger):
    print("Starting unzip process...")
    
    # Check if the zip file actually exists and has size
    if not os.path.exists(input_dir) or os.path.getsize(input_dir) == 0:
        print(f"Error: Zip file {input_dir} is missing or empty.")
        logger.error(f"Error: Zip file {input_dir} is missing or empty.")
        return

    # Create a temporary directory for extraction
    temp_dir = tempfile.mkdtemp()

    # Create local output directory
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Unpack the .zip folder to the temp directory
        print(f"Extracting {input_dir} to temp dir...")
        with ZipFile(input_dir, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        logger.info(f"Zip folder unpacked ^_^")

        # This works for both flat structures and nested folders.
        files_found = 0
        for root, _, files in os.walk(temp_dir):
            for file in files:
                if file.endswith('.gz'):
                    files_found += 1
                    print(f"Processing: {file}")

                    gz_path = os.path.join(root, file)
                    # Remove .gz extension for the output name
                    json_filename = file[:-3]  
                    output_path = os.path.join(output_dir, json_filename)

                    with gzip.open(gz_path, 'rb') as gz_file, open(output_path, 'wb') as out_file:
                        shutil.copyfileobj(gz_file, out_file)
        
        if files_found == 0:
            print("No .gz files were found in the zip archive.")
            logger.info("No .gz files were found in the zip archive.")
        else:
            print(f"Successfully processed {files_found} files.")
            logger.info(f"Successfully processed {files_found} files ^_^")

    except Exception as e:
        print(f"An error occurred during unzip: {e}")
        logger.error(f"An error occurred during unzip: {e}")
    finally:
        # Clean up temp directory even if errors occur
        shutil.rmtree(temp_dir)
