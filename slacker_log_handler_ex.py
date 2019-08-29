import logging
import os

from slacker_log_handler import SlackerLogHandler, NoStacktraceFormatter

# Create slack handler
from ex_src.sub_module import sub_module_1

'''
logging.ERROR
WARNING
'''

def hello():
    logger.info("heellloooo")

# formatter = NoStacktraceFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s - %(filename)s : %(lineno)d line - %(funcName)s - %(levelname)s - %(message)s')
log_slack_handler = SlackerLogHandler('xoxb-707533402582-707555674182-4IzzBXtLwPqNseiUSbu11s8V', '#dev', stack_trace=True)
log_slack_handler.setLevel(logging.WARNING)
log_slack_handler.setFormatter(formatter)

log_file_handler = logging.FileHandler(os.path.join('py_log', 'log.txt'))
log_file_handler.setLevel(logging.INFO)
log_file_handler.setFormatter(formatter)

log_stream_handler = logging.StreamHandler()
# log_stream_handler.setLevel(logging.INFO)
log_stream_handler.setFormatter(formatter)
# Create logger
logger = logging.getLogger(__name__)

# logger.addHandler(log_slack_handler)
logger.addHandler(log_file_handler)
logger.addHandler(log_stream_handler)

# OPTIONAL: Define a log message formatter.
# If you have set stack_trace=True, any exception stack traces will be included as Slack message attachments.
# You therefore need to use NoStacktraceFormatter as a base to exclude the trace from the main message text.



# Define the minimum level of log messages you want to send to Slack

logger.setLevel(logging.DEBUG)
logger.info("test Start")
# raise RuntimeError
# Test logging
hello()
try:
    sub_module_1()
    int('a')
except:
    logger.critical("cri")
    logger.exception("Debug message from slack!")
    # raise
logger.debug("Done")
logger.info("INFO")