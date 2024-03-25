from DateTimeUtil import DateTimeUtil

class DateTime:

    def printAllTime(dateTimeUtil):
        print("Epoch                    :   ", dateTimeUtil.getEpochTime())
        print("Epoch Milliseconds       :   ", dateTimeUtil.getEpochInMilli())
        print("Epoch Nanoseconds        :   ", dateTimeUtil.getEpochInNano())
        print("ISO Format               :   ", dateTimeUtil.getTimeInIso())
        print("ISO Format with 'T'      :   ", dateTimeUtil.getTimeInIsoT())
        print("ISO Format with timezone :   ", dateTimeUtil.getTimeInIsoWithZone())
        print("ISO Format in UTC        :   ", dateTimeUtil.getTimeInUtc())
        print("ISO Format in IST        :   ", dateTimeUtil.getTimeInIst())
        print("ISO Format in EST        :   ", dateTimeUtil.getTimeInEst())

    if __name__ == "__main__":
        printAllTime(DateTimeUtil())