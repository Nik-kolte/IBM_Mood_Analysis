from libs import mood_on_twtter, mood_facebook, mood_youtube
from db_util import retreive_data, push_data
from libs import mood_analysis
from collections import OrderedDict
from suggestion_db import suggestion_result
import datetime

def main():
	database_dict = retreive_data.retrieve_from_db("credentials")
	database_dict = database_dict[1]['doc']
	twitter_username = database_dict['twr_username']
	facebook_api_key = database_dict['fb_api_key']
	youtube_api_key = database_dict['yt_api_key']
	youtube_channel_key = database_dict['yt_channelid']
	twitter_mood_score = mood_on_twtter.mood_get_twitter(twitter_username)
	facebook_mood_score = mood_facebook.get_mood_on_facebook(facebook_api_key)
	youtube_mood_score = mood_youtube.get_mood_youtube(youtube_channel_key, youtube_api_key)
	if ((twitter_mood_score != []) or (facebook_mood_score != []) or (youtube_mood_score != [])):
		final_res_dict = OrderedDict(mood_analysis.get_mood_today(twitter_mood_score, youtube_mood_score, facebook_mood_score))
		suggestion = suggestion_result.give_suggestion(final_res_dict['prominent_emotion'])
		final_res_dict['prompt'] = suggestion[0]
		final_res_dict['quote'] = suggestion[1]
		final_res_dict['video_link'] = suggestion[2]

	else:
		final_res_dict = {}
		final_res_dict['_id'] = ((datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
		suggestion = suggestion_result.give_suggestion('Not Active')
		final_res_dict['prominent_emotion'] = 'Not_active'
		final_res_dict['prompt'] = suggestion[0]
		final_res_dict['quote'] = suggestion[1]
		final_res_dict['video_link'] = suggestion[2]



	push_data.push_my_dict(final_res_dict, "moodanalyser")


if __name__ == "__main__":
	main()
