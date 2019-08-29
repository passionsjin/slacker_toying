import traceback

import sys
from slacker import Slacker

token = 'xoxb-707533402582-707555674182-4IzzBXtLwPqNseiUSbu11s8V'
slacker = Slacker(token)

# attachments_dict = dict()
# attachments_dict['pretext'] = "attachments 블록 전에 나타나는 text"
# attachments_dict['title'] = "다른 텍스트 보다 크고 볼드되어서 보이는 title"
# attachments_dict['title_link'] = "https://corikachu.github.io"
# attachments_dict['fallback'] = "클라이언트에서 노티피케이션에 보이는 텍스트 입니다. attachment 블록에는 나타나지 않습니다"
# attachments_dict['text'] = "본문 텍스트! 5줄이 넘어가면 *show more*로 보이게 됩니다."
# attachments_dict['mrkdwn_in'] = ["text", "pretext"]  # 마크다운을 적용시킬 인자들을 선택합니다.
# attachments = [attachments_dict]
#
# slacker.chat.post_message(channel="#dev", text=None, attachments=attachments, as_user=True)


def send(msg):
    return slacker.chat.post_message(channel="#dev", text=msg, as_user=True)


def exc1():
    return exc2()


def exc2():
    return exc3()


def exc3():
    int('k')
    raise ValueError

class my_exception(Exception):



try:
    exc1()
except:
    # print(e)
    # print(''.join(traceback.format_stack()))
    # print(traceback.extract_stack())
    print(sys.exc_info()[1])
    print(traceback.format_exc())

print('end')