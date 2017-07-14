import socket
import sys
import os.path
import _thread
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from irc.irc import *
from  irc.mathParsing import NumericStringParser
import time

channel = "#mitchjones"
server = "irc.chat.twitch.tv"
nickname = "mathreplybot"
authString = "oauth:yqgirsd4liatini29kdm0fgugmkpbf"

irc = IRC()
irc.connect(server, channel, nickname,authString)
def replyDelayed(tekst,stime):
    time.sleep(stime)
    irc.send(channel, tekst)

while 1:
    text = irc.get_text()
    plaintText = text.decode()
    nsp = NumericStringParser()

    if ":arithmeticbot" in plaintText and channel in plaintText:
        #time.sleep(4)
        print(text.decode())
        crap, math = plaintText.split('MATH: ')
        finalExpression, crap = math.split(' =')
        result = nsp.eval(finalExpression)
        _thread.start_new_thread(replyDelayed, (str(int(result)),8) )
        #irc.send(channel,str(int(result)))