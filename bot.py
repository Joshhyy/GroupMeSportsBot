import requests

def postMessage(msg):
	requests.post('https://api.groupme.com/v3/bots/post', data = {'bot_id':'eab17fded6cb2af875ca468f58', 'text': msg})
postMessage('Hello, Jake!')
