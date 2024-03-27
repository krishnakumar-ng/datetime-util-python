from DateTimeParser import DateTimeParser
from DateTimeUtil import DateTimeUtil

class DateTime:

    def printAllTime(dateTimeUtil):
        print("Epoch                            :   ", dateTimeUtil.getEpochTime())
        print("Epoch Milliseconds               :   ", dateTimeUtil.getEpochInMilli())
        print("Epoch Nanoseconds                :   ", dateTimeUtil.getEpochInNano())
        print("ISO Format                       :   ", dateTimeUtil.getTimeInIso())
        print("ISO Format with timezone         :   ", dateTimeUtil.getTimeInIsoWithZone())
        print("ISO Format in UTC                :   ", dateTimeUtil.getTimeInUtc())
        print("ISO Format in IST                :   ", dateTimeUtil.getTimeInIst())
        print("ISO Format in EST                :   ", dateTimeUtil.getTimeInEst())
        print("ISO Format with 'Z'              :   ", dateTimeUtil.getTimeInIsoWithZ())
        print("ISO Format with zone Offset      :   ", dateTimeUtil.getTimeInIsoWithZoneOffset())
        print("ISO Format in UTC with 'Z'       :   ", dateTimeUtil.getTimeInUtcWithZ())
        print("ISO Format in IST with 'Z'       :   ", dateTimeUtil.getTimeInIstWithZ())
        print("ISO Format in EST with 'Z'       :   ", dateTimeUtil.getTimeInEstWithZ())
    
    if __name__ == "__main__":
        
        print("=====================================================================================")
        input_time = input("Enter the input time in any format or Enter now for the current time: \n")
        
        time = DateTimeParser.parse_input(input_time)

        printAllTime(DateTimeUtil(time))

        print("=====================================================================================")
        