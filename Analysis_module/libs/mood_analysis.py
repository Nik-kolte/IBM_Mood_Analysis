import math
import datetime


def _get_total(temp_dict):
	total_ = 0
	for t in temp_dict.keys():
		total_ += temp_dict[t]

	temp_dict['total'] = total_
	return temp_dict

def _get_weightage(freq_twr, freq_ytb, freq_fb):

	temp_list = [freq_twr[0],freq_ytb[0],freq_fb[0]]
	total = 0
	change_temp_list = []
	for temp in temp_list:
		change_temp_list.append(_get_total(temp))

	for t in change_temp_list:
		total += t['total']

	total_twr, total_ytb, total_fb = change_temp_list[0]['total'],change_temp_list[1]['total'],change_temp_list[2]['total']

	return ((total_twr/total),(total_ytb/total),(total_fb/total))


def f(v, wt):
	return v*wt


def get_mood_today(twitter_doc_score, youtube_doc_score, facebook_doc_score, id):
	twitter_freq, youtube_freq, facebook_freq = _smd_emot_count( twitter_doc_score), _smd_emot_count(youtube_doc_score), _smd_emot_count(facebook_doc_score)
	wt_twr,wt_ytb,wt_fb =_get_weightage(twitter_freq,youtube_freq,facebook_freq)

	score_twr = {k: f(v,wt_twr) for k, v in twitter_freq[1].items()}
	score_ytb = {k: f(v,wt_ytb) for k, v in youtube_freq[1].items()}
	score_fb = {k: f(v,wt_fb) for k, v in facebook_freq[1].items()}

#	print(score_twr,score_ytb,score_fb)

	final_emot_score = score_twr.copy()
	# for youtube
	for emot in score_ytb.keys():
		try:
			final_emot_score[emot] += score_ytb[emot]
		except:
			final_emot_score[emot] = score_ytb[emot]

	for emot in score_fb.keys():
		try:
			final_emot_score[emot] += score_fb[emot]
		except:
			final_emot_score[emot] = score_fb[emot]

	final_emot_score = sorted(final_emot_score.items(), key=lambda x: x[1],reverse=True)
	prom = (final_emot_score[0][0])

	final_emot_score.append(('_id',(datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')))
	final_emot_score.append(('prominent_emotion', prom))
#	final_emot_score['prominent_emotion'] = prom

#	print(final_emot_score)
	return final_emot_score



def _smd_emot_count(list_sent):
	list_emot = list()
	freq_emot = dict()
	freq_emot_score = dict()
#	print(list_sent[0]['tones'][0]['tone_name'])
	for sentence in list_sent:
		try:
			freq_emot[sentence['tones'][0]['tone_name']] = 0
		except:
			try:
				for tone in sentence['tones']:
					freq_emot[tone['tone_name']] = 0
			except:
				continue

	freq_emot_score = freq_emot.copy()
	for sentence in list_sent:
		try:
			freq_emot[sentence['tones'][0]['tone_name']] += 1
			freq_emot_score[sentence['tones'][0]['tone_name']] += sentence['tones'][0]['score']
		except:
			try:
				for tone in sentence['tones']:
					freq_emot[tone['tone_name']] += 1
					freq_emot_score[tone['tone_name']] += tone['score']

			except:
				continue
	list_emot = [freq_emot,freq_emot_score]
	return list_emot

