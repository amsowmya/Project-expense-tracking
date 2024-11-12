import logging

log_file_path = "E:\SAM\PYTHON\Code_Basics_Tutorial\Project-expense-tracking\server.log"

def setup_logger(name, log_file=log_file_path, level=logging.DEBUG):
    # Create a custom logger
    logger = logging.getLogger(name)

    # Configure the custom logger
    logger.setLevel(level)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger