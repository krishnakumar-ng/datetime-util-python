from datetime import datetime, timezone, timedelta

class DateTimeUtil:

    def __init__(self,time):
        # Current date and time
        self.time = time

    '''
    Convert to Epoch time (seconds)
    '''
    def getEpochTime(self):
        return int(self.time.timestamp())
    
    '''
    Convert to Epoch time in milliseconds
    '''
    def getEpochInMilli(self):
        return int(round(self.time.timestamp() * 1000))
    
    '''
    Convert to Epoch time in nanoseconds
    '''
    def getEpochInNano(self):
        return int(self.time.timestamp() * 1e9)

    '''
    Convert to ISO 8601 format
    '''
    def getTimeInIso(self):
        return self.time.isoformat()

    '''
    Convert to ISO 8601 format with timezone
    '''
    def getTimeInIsoWithZone(self):
        return self.time.astimezone().isoformat()

    '''
    Convert to ISO 8601 format in UTC
    '''
    def getTimeInUtc(self):
        return self.time.astimezone(timezone.utc).isoformat()
    
    '''
    Convert to ISO 8601 format in Indian Standard Time (IST)
    '''
    def getTimeInIst(self):
        return self.time.astimezone(timezone(timedelta(hours=5,minutes=30))).isoformat()
    
    '''
    Convert to ISO 8601 format in Eastern Standard Time (EST)
    '''
    def getTimeInEst(self):
        return self.time.astimezone(timezone(timedelta(hours=-5))).isoformat()

    '''
    Convert to ISO 8601 format with 'Z'
    '''
    def getTimeInIsoWithZ(self):
        return self.time.isoformat(timespec='seconds') + 'Z'
    
    '''
    Convert to ISO 8601 format with timezone offset as 'z'
    '''
    def getTimeInIsoWithZoneOffset(self):
        return self.time.isoformat(timespec='milliseconds') + self.time.strftime('%z')
    
    '''
    Convert to ISO 8601 format in UTC with 'Z'
    '''
    def getTimeInUtcWithZ(self):
        return self.time.astimezone(timezone.utc).isoformat() + 'Z'
    
    '''
    Convert to ISO 8601 format in UTC with 'Z'
    '''
    def getTimeInIstWithZ(self):
        return self.time.astimezone(timezone(timedelta(hours=5,minutes=30))).isoformat() + 'Z'
    
    '''
    Convert to ISO 8601 format in UTC with 'Z'
    '''
    def getTimeInEstWithZ(self):
        return self.time.astimezone(timezone(timedelta(hours=-5))).isoformat() + 'Z'