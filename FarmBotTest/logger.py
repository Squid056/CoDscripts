import logging

# https://docs.python.org/3/library/logging.html#

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(level=logging.DEBUG)
#                                time       module         line in module   log level        message
formatter =  logging.Formatter("{asctime} : {module:<15} : {lineno:04d} : {levelname:^15} : {message}", style="{")
sh.setFormatter(formatter)

logger.addHandler(sh)

fh = logging.FileHandler("bot.log") # log file
fh.setLevel(level=logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
