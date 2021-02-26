from app.utils.response_body import response_body
from app import db
import logging


LOGGER_FORMAT = "%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(level=logging.DEBUG, format=LOGGER_FORMAT, datefmt=DATE_FORMAT, )
# logger = logging.getLogger('resources')
