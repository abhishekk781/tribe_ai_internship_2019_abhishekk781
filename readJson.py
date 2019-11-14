import json
import codecs

def readJson(fileLocation):
	jsonData = json.load(codecs.open(fileLocation, 'r', 'utf-8-sig'))
	return jsonData

def getValue(dic, keyList):
	if(len(keyList)==1):
		return dic[keyList[0]]
	else:
		return getValue(dic[keyList[0]], keyList[1:])
