import os
import sys
import logging

logDir="logs"

loggingStr="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
loggingFilepath = os.path.join(logDir,"running_logs.log")

os.makedirs(logDir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=loggingStr,
    handlers=[
        logging.FileHandler(loggingFilepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger= logging.getLogger('summarizerLogger')