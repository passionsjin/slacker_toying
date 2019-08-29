from slacker import Slacker

from config.keys import slack_token

slacker = Slacker(slack_token)

channel = '#dev'
as_user = True

param = {'channel': '',
         'level': 'error warning notify..',
         'msg': ''}


def normal_function(msg):
    pass


def error_function(msg):
    pass


def send_msg(msg):
    return slacker.chat.post_message(channel=channel, text=msg, as_user=as_user)


def send_msg_dict(msg: dict):
    return slacker.chat.post_message(**msg)


if __name__ == '__main__':
    '''
    {
    "attachments": [
        {
            "fallback": "Required plain-text summary of the attachment.",
            "color": "#36a64f",
            "pretext": "Optional text that appears above the attachment block",
            "author_name": "Bobby Tables",
            "author_link": "http://flickr.com/bobby/",
            "author_icon": "http://flickr.com/icons/bobby.jpg",
            "title": "Slack API Documentation",
            "title_link": "https://api.slack.com/",
            "text": "Optional text that appears within the attachment",
            "fields": [
                {
                    "title": "Priority",
                    "value": "High",
                    "short": false
                }
            ],
            "image_url": "http://my-website.com/path/to/image.jpg",
            "thumb_url": "http://example.com/path/to/thumb.png",
            "footer": "Slack API",
            "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
            "ts": 123456789
        }
    ]
    "channel": ,
    "as_user": True,
    "text": None
}
    '''
    attachments_dict = {'pretext': '**요** ***약***',
                        'title': '제목?',
                        'title_link': '', # 제목에 링크 걸수있음.
                        'fallback': '노티에서 보이는거??',
                        'text': '#본문쓰으으으으##마크다운?',
                        'mrkdwn_in': ['text', 'pretext']    # 이건 안되는듯???
                        }
    msg_param = {'attachments': [attachments_dict],
                 'channel': '#dev',
                 'text': 'Text?????',
                 'as_user': True}
    # print(send_msg_dict({'channel': '#dev', 'text': 'dict', 'as_user': True}))
    print(send_msg_dict(msg_param))
