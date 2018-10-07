from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import json

client = Cloudant("03a69d8a-f9d5-49d7-8556-08476341b5e9-bluemix", "d6067fc7c571b682268c21f4a884c1d1595d96395babb86b196af8ac6f4e0ef6", url="https://03a69d8a-f9d5-49d7-8556-08476341b5e9-bluemix:d6067fc7c571b682268c21f4a884c1d1595d96395babb86b196af8ac6f4e0ef6@03a69d8a-f9d5-49d7-8556-08476341b5e9-bluemix.cloudant.com")
client.connect()

databaseName = 'moodanalyser2'
myDatabase = client.create_database(databaseName)
#newDict = {}
def push_my_dict(dict1):
	newDict = json.dumps(dict1)
	print(type(dict1)) 
	resultDocument = myDatabase.create_document(dict1)
	if resultDocument.exists():
		print ("Uploaded Successfuly.")


push_my_dict(dict_received)