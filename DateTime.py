from util.DateTimeParser import DateTimeParser
from util.DateTimeUtil import DateTimeUtil
import json

class DateTime:

    def printAllTime(dateTimeUtil):
        output = {
        "Epoch Current Time": dateTimeUtil.getEpochTime(),
        "Epoch Milliseconds": dateTimeUtil.getEpochInMilli(),
        "Epoch Nanoseconds": dateTimeUtil.getEpochInNano(),
        "Epoch_Today_Start": dateTimeUtil.getEpochForStartOfTheDay(),
        "Epoch_Today_End": dateTimeUtil.getEpochForEndOfTheDay(),
        "Epoch_24_Hrs_Forward": dateTimeUtil.getEpochFor24HoursForward(),
        "Epoch_24_Hrs_Back": dateTimeUtil.getEpochFor24HoursBack(),
        "ISO Format": dateTimeUtil.getTimeInIso(),
        "ISO Format with timezone": dateTimeUtil.getTimeInIsoWithZone(),
        "ISO Format in UTC": dateTimeUtil.getTimeInUtc(),
        "ISO Format in IST": dateTimeUtil.getTimeInIst(),
        "ISO Format in EST": dateTimeUtil.getTimeInEst(),
        "ISO Format with 'Z'": dateTimeUtil.getTimeInIsoWithZ(),
        "ISO Format with zone Offset": dateTimeUtil.getTimeInIsoWithZoneOffset(),
        "ISO Format in UTC with 'Z'": dateTimeUtil.getTimeInUtcWithZ(),
        "ISO Format in IST with 'Z'": dateTimeUtil.getTimeInIstWithZ(),
        "ISO Format in EST with 'Z'": dateTimeUtil.getTimeInEstWithZ(),
        "Week of the year": dateTimeUtil.getWeekOfTheYear()
        }
        print(json.dumps(output, indent=4))
    
    if __name__ == "__main__":
        
        print("=====================================================================================")
        input_time = input("Enter the input time in any format or Enter now for the current time: \n")
        
        time = DateTimeParser.parse_input(input_time)

        printAllTime(DateTimeUtil(time))

        print("=====================================================================================")
        