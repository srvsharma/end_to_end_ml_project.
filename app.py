import sys
import sys
sys.path.append("src")  

from end_to_end_ml_project.logger import logging
from end_to_end_ml_project.exception import CustomException

if __name__ == "__main__":
    logging.info("The execution has started")


    try:
        a = 1/0

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
