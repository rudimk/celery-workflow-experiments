import arrow

def getCurrentTime():
    return arrow.now().to('Asia/Kolkata').format('DD-MMM-YYYY HH:mm:ss ZZ')

def getZoneTime(tz):
    return arrow.now().to(tz).format('DD-MMM-YYYY HH:mm:ss ZZ')