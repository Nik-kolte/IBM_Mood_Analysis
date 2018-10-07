import urllib.request
#import urlopen
import json
import re
from datetime import date,timedelta
from . import sentiment_score
validDate = date.today() - timedelta(1)
likeDict = {}
likeList = []
newTitle = ''
newDesc = ''

def find_youtube_results(channel_id,api_key):
	url = "https://www.googleapis.com/youtube/v3/activities?part=snippet,contentDetails&channelId=" + channel_id + "&key="+ api_key +"&maxResults=50"
	content =urllib.request.urlopen(url)
	string1 = content.read().decode('utf-8')
	youtube_doc = ''
	decode = json.loads(string1)

	mylist = decode['items']

	for i in mylist:
		actionType = i['snippet']['type']
		prevDate = i['snippet']['publishedAt'][:10]
		if actionType == 'like' and prevDate == str(validDate):
			timePublishedval = i['snippet']['publishedAt'][:10]
			videoIDval = i['contentDetails']['like']['resourceId']['videoId']
			videoDescval = i['snippet']['description']
			videoTitleval = i['snippet']['title']
			for k in videoTitleval.split("\n"):
				newTitle = re.sub(r"[^a-zA-Z0-9]+", ' ', k)

			for k in videoDescval.split("\n"):
				newDesc = re.sub(r"[^a-zA-Z0-9]+", ' ', k)

			youtube_doc = youtube_doc+videoTitleval+"."+videoDescval+"."
			#print(likeDict)
			likeList.append(likeDict)
		elif actionType == 'subscription' and prevDate == str(validDate):
			timePublishedval = i['snippet']['publishedAt'][:10]
			channelIDval = i['contentDetails']['subscription']['resourceId']['channelId']
			channelTitleval = i['snippet']['channelTitle']
		else:
			continue

	if youtube_doc != "":
		return(youtube_doc)
	else:
		print("No History.")
		return("")


def get_mood_youtube(channel_id,api_key):
	return sentiment_score.mood_sentiment_score(find_youtube_results(channel_id,api_key))
