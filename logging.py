import logging
import os
from datetime import datetime

def logging_function(prefix, timestamp):
    '''
    Sets up the files
    
    :param prefix: The folder name for the logs
    :param timestamp: The name of the log files
    '''
    dir = f'{prefix}_logs'
    
    os.makedirs(dir, exist_ok=True)

    #created the log file using the file name
    log_filename = f"{dir}/{timestamp}.log"

    # configures the log file
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_filename
    )

    return logging.getLogger()