import logging
import os

from from_root import from_root
from datetime import datetime

project_root = "D:\MLOps_Project1\MLOps_project1_visa_approval"

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

logs_dir_path = os.path.join(project_root, log_dir)

os.makedirs(logs_dir_path, exist_ok=True)

logs_file_path = os.path.join(logs_dir_path, LOG_FILE)

logging.basicConfig(
    filename=logs_file_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)