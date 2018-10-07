from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import ToneAnalyzerV3
import logging
import json
#watson_reply = ''


tone_analyzer = ToneAnalyzerV3(
 url = "https://gateway.watsonplatform.net/tone-analyzer/api",
 username =  "0ff63961-ce99-45e4-ab30-a045d602cea8",
 password = "0aXnZChrVZH1",
   version = "2017-09-21"
)

def mood_sentiment_score(text):
#	print(text)
	try:
		tone_analysis = tone_analyzer.tone({"text":text},'application/json').get_result()
#	print(tone_analysis)
		if ("sentences_tone" in (tone_analysis.keys())):
			return tone_analysis['sentences_tone']

		return tone_analysis['document_tone']['tones']
	except:
#		logging.exception('No Text.. {}'.format(e))
		return []

