import traceback

# class MyException(Exception):
#     MYEXCEPTIONS = {'error_key': 'msg', 'NoExistKey': 'No Exist Key'}
#
#     def __init__(self, error_key):
#         super().__init__(error_key)
#
#         if error_key not in self.MYEXCEPTIONS:
#             raise self.__init__('NoExistKey')
#
#         # print('except %s ' % self.MYEXCEPTIONS[error_key])
#         print(sys.exc_info()[1])
#         print(traceback.format_exc())

from py_log import cm_logger


class CMException(Exception):
    def __init__(self):
        cm_logger.logger.exception('CM')
        # t_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # exception_title = str(sys.exc_info()[1]) if exception_title is None else exception_title
        # exception_body = str(traceback.format_exc()) if exception_body is None else exception_body
        # send_msg_dict(slack_error_message_dict(exception_title=exception_title,
        #                                        exception_body=exception_body,
        #                                        module_name=module_name,
        #                                        msg='[%s]' % t_time if msg is None else '[%s] %s' % (t_time, msg),
        #                                        error_level=error_level))
        # print(exception_body)


def slack_error_message_dict(exception_title, exception_body, module_name, msg=None, error_level=1):
    '''

    :param exception_title:
    :param exception_body:
    :param module_name: 실행중인 module 이름
    :param msg:
    :param error_level: 에러 레벨 (1: 보통 2: 심각 3: 아주 심각 )
    :return:
    '''

    return {"attachments": [
        {
            "fallback": "ERROR [%s]" % module_name,
            "color": "#ff0000", # Red
            "pretext": "ERROR in [ %s ] " % module_name,
            "title": exception_title,
            "text": exception_body,
        }], "channel": '#dev', "as_user": True, "text": msg
    }

def get_traceback():
    print('traceback-------')
    print(traceback.print_last())
    print('-' * 10)


if __name__ == '__main__':
    # print("start")
    # get_traceback()
    # print('-' * 20)
    try:
        int('k')
    except Exception as e:
        MyException('error_key')

    # try:
    #     print('raise')
    #     raise MyException('error_key')
    # except Exception as e:
    #     print('30 %s' % e)
        # get_traceback()
        # MyException(e)
    # get_traceback()
    print('end')