import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    #get the name of the class
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    #by default,log all messages
    logger.setLevel(logging.DEBUG)

    filehandler = logging.FileHandler("automation.log",mode='a')
    filehandler.setLevel(logLevel)

    formatter = logging.Formatter('%(time)s - %(name)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    return logger