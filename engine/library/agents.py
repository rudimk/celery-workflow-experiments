import requests as r

def getAgent(obj, eng):
	obj['data']['agent'] = r.get('http://pplapi.com/random.json').json()

def getAgentByCountry(obj, eng):
    url = "http://pplapi.com/country/" + obj['country'] + "/random.json"
    obj['agents'].append(r.get(url).json())