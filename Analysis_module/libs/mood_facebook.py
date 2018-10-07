import requests
import urllib3
import json
import facebook
import datetime
import re
from datetime import date,timedelta
from . import sentiment_score


#token = 'EAADlOftOhGsBAOt51dqQ7pcHxPRVYwrEZAIWZC9mKZAWgz3YUJprNMEeXq3sZAZCUnElTrKpat7NLoTW87U7ylO9qT7r9BZAEe0YVlDGQ97ZCZA1MUSSvdw60JwcFZAQIwg2VpTm3F82Vx4LOdbpOQZAgfMjcsjeifxGmBWPDJhvRHLQZDZD'


def _get_date_():
    date_time = datetime.datetime.now() - datetime.timedelta(days=1)
    return date_time.strftime('%Y-%m-%d')

valid_date =  _get_date_()

def likes(token):
   like = "https://graph.facebook.com/v3.1/me?fields=likes.summary(true)&access_token="+token
   get_likes = requests.get(like)
   likes1 = get_likes.json()
   likes2 = json.dumps(likes1)
   likes3 = json.loads(likes2)
   likelist = likes3['likes']
   likes_doc = ''

   for dic in likelist['data']:
       try:
           temp1 = dic['name']
           likes_doc = likes_doc + temp1 + ". "
       except:
           continue

   #print(likes_doc)

   return(likes_doc)


def posts(token):
    post = "https://graph.facebook.com/v3.1/me?fields=posts.summary(true).since("+valid_date+")&access_token=" + token
    get_post = requests.get(post)
    post1 = get_post.json()
    post2 = json.dumps(post1)
    post3 = json.loads(post2)    
    message_doc = ''
    if "posts" in post3:
        postlist = post3['posts']
        for dic in postlist['data']:
            try:
                temp = dic['message']
                temp_list = (temp.split('\n'))
                message = " ".join(l for l in temp_list)                
                message_doc = message_doc + " ".join(
                    re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", message).split()) + ". "
            except:
                continue

        #print(message_doc)
        return (message_doc)
    else:
        # print ("Empty")
        return (message_doc)




def get_mood_on_facebook(token):
   return (sentiment_score.mood_sentiment_score(posts(token)))
