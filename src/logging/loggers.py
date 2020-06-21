import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
logger = logging.getLogger(__name__)
logger.debug("this is a debug message")
logger.info("this is a info message")
logger.error("this is a error message")
logger.warning("this is a warning message")
logger.critical("this is a critical message")
