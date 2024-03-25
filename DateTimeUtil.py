from datetime import datetime, timezone, timedelta

class DateTimeUtil:

    def __init__(self):
        # Current date and time
        self.current_time = datetime.now()

    '''
    Convert to Epoch time (seconds)
    '''
    def getEpochTime(self):
        return int(self.current_time.timestamp())
    
    '''
    Convert to Epoch time in milliseconds
    '''
    def getEpochInMilli(self):
        return int(round(self.current_time.timestamp() * 1000))
    
    '''
    Convert to Epoch time in nanoseconds
    '''
    def getEpochInNano(self):
        return int(self.current_time.timestamp() * 1e9)

    '''
    Convert to ISO 8601 format
    '''
    def getTimeInIso(self):
        return self.current_time.isoformat();

    '''
    Convert to ISO 8601 format with 'T'
    '''
    def getTimeInIsoT(self):
        return self.current_time.isoformat(timespec='seconds') + "T"

    '''
    Convert to ISO 8601 format with timezone
    '''
    def getTimeInIsoWithZone(self):
        return self.current_time.astimezone().isoformat()

    '''
    Convert to ISO 8601 format in UTC
    '''
    def getTimeInUtc(self):
        return self.current_time.astimezone(timezone.utc).isoformat()
    
    '''
    Convert to ISO 8601 format in Indian Standard Time (IST)
    '''
    def getTimeInIst(self):
        return self.current_time.astimezone(timezone(timedelta(hours=5,minutes=30))).isoformat()
    
    '''
    Convert to ISO 8601 format in Eastern Standard Time (EST)
    '''
    def getTimeInEst(self):
        return self.current_time.astimezone(timezone(timedelta(hours=-5))).isoformat();
