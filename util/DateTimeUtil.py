from datetime import datetime, timezone, timedelta

class DateTimeUtil:

    def __init__(self,time):
        # Current date and time
        self.time = time

        # Determine if current date is within daylight saving time period (2nd Sunday of March to 1st Sunday of November)
        # Determine the offset for Eastern Time (ET)
        if datetime(self.time.year, 3, 8) <= self.time.replace(tzinfo=None) < datetime(self.time.year, 11, 1):
            self.est_offset = -4  # Daylight Saving Time (EDT) = UTC-4
        else:
            self.est_offset = -5  # Standard Time (EST) = UTC-5

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
        return self.time.astimezone(timezone(timedelta(hours=self.est_offset))).isoformat()

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
        return self.time.astimezone(timezone(timedelta(hours=self.est_offset))).isoformat() + 'Z'
    

    def getEpochForStartOfTheDay(self):
        start_of_day = datetime(self.time.year, self.time.month, self.time.day, 0, 0, 0)
        return int(start_of_day.timestamp())

    def getEpochForEndOfTheDay(self):
        end_of_day = datetime(self.time.year, self.time.month, self.time.day, 23, 59, 59)
        return int(end_of_day.timestamp())

    def getEpochFor24HoursBack(self):
        twenty_four_hours_back = self.time - timedelta(hours=24)
        return int(twenty_four_hours_back.timestamp())

    def getEpochFor24HoursForward(self):
        twenty_four_hours_forward = self.time + timedelta(hours=24)
        return int(twenty_four_hours_forward.timestamp())