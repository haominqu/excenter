from django.shortcuts import render

from dwebsocket.decorators import accept_websocket
from collections import defaultdict

# Create your views here.
allconn = defaultdict(list)


def send_web_msg(user_id,msg):
    for i in allconn:
        if i != user_id:
            allconn[i].send(msg)
    return True