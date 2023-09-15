from DogSegmentation.logger import logging
from DogSegmentation.exception import AppException
import sys

logging.info("Welcome to the custom log")

try:
    a = 10/"6"

except Exception as e:
    raise AppException(e,sys)
