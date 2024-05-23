import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# logpath uses the path.join functions to make the folder where file will be save
logpath=os.path.join(os.getcwd(),"logs")

# now make the direcotry
os.makedirs(logpath,exist_ok=True)

# now put the file into path
Log_filepath=os.path.join(logpath,LOG_FILE)

logging.basicConfig(level=logging.INFO,
                    filename=Log_filepath,
                    format="[%(asctime)s]%(lineno)d%(name)s-%(levelname)s-%(message)s")


#logging.error("why this is not callable?")
