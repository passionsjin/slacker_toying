import logging
from slacker_log_handler import SlackerLogHandler

# Create slack handler

__log_slack_handler = SlackerLogHandler('xoxb-707533402582-707555674182-4IzzBXtLwPqNseiUSbu11s8V', '#dev', stack_trace=True)
__formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
__log_slack_handler.setFormatter(__formatter)
__log_slack_handler.setLevel(logging.DEBUG)

__log_file_handler = logging.FileHandler('log.txt')
__log_file_handler.setLevel(logging.INFO)
__log_file_handler.setFormatter(__formatter)

__log_stream_handler = logging.StreamHandler()
__log_stream_handler.setLevel(logging.INFO)
__log_stream_handler.setFormatter(__formatter)
# Create logger
logger = logging.getLogger('debug_application')
logger.addHandler(__log_slack_handler)
logger.addHandler(__log_file_handler)
logger.addHandler(__log_stream_handler)

# OPTIONAL: Define a log message formatter.
# If you have set stack_trace=True, any exception stack traces will be included as Slack message attachments.
# You therefore need to use NoStacktraceFormatter as a base to exclude the trace from the main message text.
# __formatter = NoStacktraceFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Define the minimum level of log messages you want to send to Slack

