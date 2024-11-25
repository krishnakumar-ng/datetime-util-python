from util.DateTimeParser import DateTimeParser
from util.DateTimeUtil import DateTimeUtil
import json

class DateTime:

    def printAllTime(dateTimeUtil):
        output = {
        "Epoch": dateTimeUtil.getEpochTime(),
        "Epoch Milliseconds": dateTimeUtil.getEpochInMilli(),
        "Epoch Nanoseconds": dateTimeUtil.getEpochInNano(),
        "Epoch_Start_Of_The_Day": dateTimeUtil.getEpochForStartOfTheDay(),
        "Epoch_End_Of_The_Day": dateTimeUtil.getEpochForEndOfTheDay(),
        "Epoch_24_Hrs_Forward": dateTimeUtil.getEpochFor24HoursForward(),
        "Epoch_24_Hrs_Back": dateTimeUtil.getEpochFor24HoursBack(),
        "ISO Format": dateTimeUtil.getTimeInIso(),
        "ISO Format with timezone": dateTimeUtil.getTimeInIsoWithZone(),
        "ISO Format in UTC": dateTimeUtil.getTimeInUtc(),
        "ISO Format in IST": dateTimeUtil.getTimeInIst(),
        "ISO Format in EST": dateTimeUtil.getTimeInEst(),
        "ISO Format in PST": dateTimeUtil.getTimeInPst(),
        "ISO Format in EET": dateTimeUtil.getTimeInEet(),
        "ISO Format with 'Z'": dateTimeUtil.getTimeInIsoWithZ(),
        "ISO Format with zone Offset": dateTimeUtil.getTimeInIsoWithZoneOffset(),
        "ISO Format in UTC with 'Z'": dateTimeUtil.getTimeInUtcWithZ(),
        "ISO Format in IST with 'Z'": dateTimeUtil.getTimeInIstWithZ(),
        "ISO Format in EST with 'Z'": dateTimeUtil.getTimeInEstWithZ(),
        "ISO Format in PST with 'Z'":dateTimeUtil.getTimeInPstWithZ(),
        "ISO Format in EET with 'Z'":dateTimeUtil.getTimeInEetWithZ(),
        "Week of the year": dateTimeUtil.getWeekOfTheYear()
        }
        print(json.dumps(output, indent=4))
    
    if __name__ == "__main__":
        
        print("=====================================================================================")
        print("Available Input formats: \n"
              "1. Enter now for the current time\n"
              "2. Enter the input time in any format\n"
              "3. Enter add X mins/hours/days/weeks/yrs to add X to the current time\n"
              "4. Enter subtract/sub X mins/hours/days/weeks/yrs to subtract X from the current time\n")
        
        input_time = input("Enter the input time in one of the above format: ")
        
        time = DateTimeParser.parse_input(input_time)

        printAllTime(DateTimeUtil(time))

        print("=====================================================================================")
        
