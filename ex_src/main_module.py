import logging.config

# sub_module_1()
import time
from datetime import datetime

from ex_src import env
from ex_src.call_multi_sc import call_this
from ex_src.sub_module import sub_module_1
from py_log.log_config import *

# logging.config.dictConfig(LOGCONFIG)
# logger = logging.getLogger("prod")
print(datetime.now())
print(sub_module_1())
print(call_this)
print(env)
# print(str(logger.handlers[1]))
# logger.debug('A debug')
# logger.info('A info')
# logger.critical('A critical')
# logger.exception('A exception')