import time

from ex_src.call_multi_sc import call_this
from ex_src.sub2_module import sub_module_2
from my_exception import CMException


def sub_module_1():
    # raise CMException()
    print(sub_module_2())
    time.sleep(1)
    print(call_this)
    call_this.join('1')
    print(call_this)
    return str(__name__)