import requests as r

def getAgent():
    return r.get('http://pplapi.com/random.json').json()

def getAgentByCountry(country):
    url = "http://pplapi.com/country/" + country + "/random.json"
    return r.get(url).json()