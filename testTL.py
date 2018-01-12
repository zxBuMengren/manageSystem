# *_* coding:utf-8 *_*

import sys
import requests

reload(sys)
sys.setdefaultencoding('utf8')

print u">>>你好,我是自动聊天机器人！"

while 1:
    text = raw_input('>>>')
    result = requests.post("http://www.tuling123.com/openapi/api",data={
        "key":"c27a6767344f4b03954fbb0debb16348",
        "info":text,
        "userid":'zx123456'})
    result = result.json()
    print result["text"]