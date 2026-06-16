import requests
import os

TOKEN = os.getenv("PUSHPLUS_TOKEN")

def send(msg):
    url = "http://www.pushplus.plus/send"

    data = {
        "token": TOKEN,
        "title": "📊 Level 5 投资信号",
        "content": msg,
        "template": "txt"
    }

    requests.post(url, json=data)