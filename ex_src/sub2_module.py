import time

from ex_src.call_multi_sc import call_this


def sub_module_2():
    time.sleep(1)
    print(call_this)
    return str(__name__)