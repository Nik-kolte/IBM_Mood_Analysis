import pandas as pd
import json
from .twitter_scraper import get_tweets
import tweepy
import datetime
import re as reg
import logging
from . import sentiment_score

UID = None
PROFILE_NAME = None


def initialize_tweet_obj(access_token, access_token_secret, consumer_key, consumer_key_secret):
	auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_key_secret)
	auth.set_access_token(access_token,access_token_secret)
	api = tweepy.API(auth) #twitter api object initialize
	return api

def _extract_user_id_name(api):
	user = api.me()
	profile_name = user.screen_name
	id_val = user.id
	PROFILE_NAME = profile_name
	UID = user.id

def _get_date_():
	date_time = datetime.datetime.now() - datetime.timedelta(days=1)
	return date_time.strftime('%Y-%m-%d')

def get_tweets_by_username(username):

	user_tweets = list(get_tweets(username, 1))
#	print(user_tweets)
	user_tweet_dict = dict(zip(list(range(1, len(user_tweets))), user_tweets))
	df = pd.DataFrame(user_tweet_dict, columns=user_tweet_dict.keys()).T
	df = df.infer_objects()
	df['time'] = pd.DatetimeIndex(df.time)
	df['date'] = df.time.dt.strftime('%Y-%m-%d')
	date_str = _get_date_()
	print(date_str  )
	df = df[df.date == date_str]
	list_tweets = list(df.text)
	tweet_doc = ""
	for tweet in list_tweets:
		tweet_doc = tweet_doc + " ".join(reg.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split()) + ". "
#	print(tweet_doc)
#	print(tweet_doc)
	return tweet_doc


def get_tweets_of_today(api=None,username=PROFILE_NAME):
	if username == None:
		_extract_user_id_name(api)
		username = PROFILE_NAME
		user_id = UID
	return get_tweets_by_username(username)


def retweets_today(api):
	retweets = api.retweets_of_me(id_=[UID])
	retweet_dict = dict()
	i = 1
	for re in retweets:
		json_str = json.dumps(re._json)
		retweet_dict[i] = json.loads(json_str)
		i = i+1
	retweet_doc = ""
	for k in retweet_dict.keys():
		retweet_doc = retweet_doc + "".join(reg.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",retweet_dict[k]['text']).split()) + ". "
	return retweet_doc

#get_tweets_of_today(username="PhilLanger2")

#print(sentiment_score.get_sentiment_score(get_tweets_of_today(username="PhilLanger2")))

#if __name__ == '__main__':
#	print(get_tweets_of_today(username="PhilLanger2"))

def mood_get_twitter(user_name):
	logging.debug("Analyzing Mood on Twitter by Tweets.. for user {}".format(user_name))
	return sentiment_score.mood_sentiment_score(get_tweets_of_today(username=user_name))
