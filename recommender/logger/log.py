import logging
import os
from datetime import datetime

log_dir="logs"
log_dir=os.path.join(os.getcwd(), log_dir)
os.makedirs(log_dir, exist_ok=True)

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_name = f"log_{current_time}.log"
log_file_path = os.path.join(log_dir, log_file_name)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s',
    filemode='w'
)