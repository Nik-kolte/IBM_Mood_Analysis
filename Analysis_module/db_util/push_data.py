from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import json
import logging

client = Cloudant("03a69d8a-f9d5-49d7-8556-08476341b5e9-bluemix", "d6067fc7c571b682268c21f4a884c1d1595d96395babb86b196af8ac6f4e0ef6", url="https://03a69d8a-f9d5-49d7-8556-08476341b5e9-bluemix:d6067fc7c571b682268c21f4a884c1d1595d96395babb86b196af8ac6f4e0ef6@03a69d8a-f9d5-49d7-8556-08476341b5e9-bluemix.cloudant.com")
client.connect()
#db = client.get()

#databaseName = 'moodanalyser2'
#newDict = {}
def push_my_dict(dict1,databaseName):
	newDict = json.dumps(dict1)
	myDatabase = client.create_database(databaseName,throw_on_exists=False)
	resultDocument = myDatabase.create_document(dict1, throw_on_exists=False)
	if resultDocument.exists():
		logging.debug("Uploaded Successfuly.. DB - {}".format(databaseName))
	client.disconnect()

#push_my_dict({"Hoola":"Haha"},'moodanalyser')