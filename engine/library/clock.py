import arrow

def getCurrentTime(obj, eng):
	obj['data']['currentTime'] = arrow.now().to('Asia/Kolkata').format('DD-MMM-YYYY HH:mm:ss ZZ')

def getZoneTime(obj, eng):
    obj['data']['zonedTime'] = arrow.now().to(obj['tz']).format('DD-MMM-YYYY HH:mm:ss ZZ')