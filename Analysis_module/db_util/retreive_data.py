from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import json

client = Cloudant("03a69d8a-f9d5-49d7-8556-08476341b5e9-bluemix", "d6067fc7c571b682268c21f4a884c1d1595d96395babb86b196af8ac6f4e0ef6", url="https://03a69d8a-f9d5-49d7-8556-08476341b5e9-bluemix:d6067fc7c571b682268c21f4a884c1d1595d96395babb86b196af8ac6f4e0ef6@03a69d8a-f9d5-49d7-8556-08476341b5e9-bluemix.cloudant.com")
client.connect()


def retrieve_from_db(databaseName ):
	myDatabase = client.create_database(databaseName,throw_on_exists = False)
	if myDatabase.exists():
#		print(databaseName)
		result_collection = list(Result(myDatabase.all_docs, include_docs=True))
		result_dict = dict(zip(list(range(0, len(result_collection))), result_collection))
#		print(result_dict)
	else:
		print("Database not Found.")
	client.disconnect()
	return  result_dict

#retrieve_from_db('credentials')#retrieve_from_db('moodanalyser1')