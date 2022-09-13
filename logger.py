import logging 

def logger(name):
    console_formatting_string = "%(asctime)s %(name)s: %(message)s"
    if name in ("bot", "parser"):
        console_formatting_string = "%(asctime)s %(message)s"
    
    console_formatter = logging.Formatter(console_formatting_string)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO)
     
    file_formatter = logging.Formatter("%(asctime)s %(message)s")
    file_handler = logging.FileHandler(f"logs/{name}.log")
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger