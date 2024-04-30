import sys
import re
from datetime import datetime, timezone, timedelta

class DateTimeParser:

    def numberOfDaysForGivenYears(years):
        # Get the current year
        currentYear = datetime.now(timezone.utc).year

        # Calculate the target year after adding the specified number of years
        targetYear = currentYear + years

        # Initialize the number of days to add
        totalDays = years * 365

        # Adjust for leap years
        for year in range(currentYear, targetYear):
            if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                totalDays += 1
        
        return totalDays


    @staticmethod
    def parse_input(input_time):
        try:
            pattern = r'\b\d+\b'

            # Try to parse input time as an integer (epoch time)
            if input_time.lower() == "now":
                return datetime.now(timezone.utc)
            
            elif input_time.lower().startswith("add"):

                integer = int(re.search(pattern, input_time).group())
                
                if input_time.lower().endswith("minutes") or input_time.lower().endswith("mins") or input_time.lower().endswith("minute") or input_time.lower().endswith("min"):
                    time = datetime.now(timezone.utc) + timedelta(minutes=integer)
                if input_time.lower().endswith("hours") or input_time.lower().endswith("hrs") or input_time.lower().endswith("hour") or input_time.lower().endswith("hr"):
                    time = datetime.now(timezone.utc) + timedelta(hours=integer)
                if input_time.lower().endswith("days") or input_time.lower().endswith("day"):
                    time = datetime.now(timezone.utc) + timedelta(days=integer)
                if input_time.lower().endswith("weeks") or input_time.lower().endswith("week"):
                    time = datetime.now(timezone.utc) + timedelta(weeks=integer)
                if input_time.lower().endswith("years") or input_time.lower().endswith("yrs") or input_time.lower().endswith("year") or input_time.lower().endswith("yr"):
                    time = datetime.now(timezone.utc) + timedelta(days=DateTimeParser.numberOfDaysForGivenYears(integer))
                
                return time

            elif input_time.lower().startswith("subtract") or input_time.lower().startswith("sub"):

                integer = int(re.search(pattern, input_time).group())

                if input_time.lower().endswith("minutes") or input_time.lower().endswith("mins") or input_time.lower().endswith("minute") or input_time.lower().endswith("min"):
                    time = datetime.now(timezone.utc) + timedelta(minutes=-integer)
                if input_time.lower().endswith("hours") or input_time.lower().endswith("hrs") or input_time.lower().endswith("hour") or input_time.lower().endswith("hr"):
                    time = datetime.now(timezone.utc) + timedelta(hours=-integer)
                if input_time.lower().endswith("days") or input_time.lower().endswith("day"):
                    time = datetime.now(timezone.utc) + timedelta(days=-integer)
                if input_time.lower().endswith("weeks") or input_time.lower().endswith("week"):
                    time = datetime.now(timezone.utc) + timedelta(weeks=-integer)
                if input_time.lower().endswith("years") or input_time.lower().endswith("yrs") or input_time.lower().endswith("year") or input_time.lower().endswith("yr"):
                    time = datetime.now(timezone.utc) + timedelta(days=-DateTimeParser.numberOfDaysForGivenYears(integer))

                return time
            
            elif input_time.isdigit():

                if len(input_time) == 13:
                    # If input is a 13-digit number, assume it's epoch time in milliseconds
                    return datetime.fromtimestamp(int(input_time) / 1000)
                elif len(input_time) == 19:
                    # If input is a 19-digit number, assume it's epoch time in nanoseconds
                    # Divide by 1e6 to convert nanoseconds to milliseconds
                    return datetime.fromtimestamp(int(input_time) / 1e9)
                else:
                    # If the input is not 13 or 19 digits, assume it's epoch time in seconds
                    return datetime.fromtimestamp(int(input_time))

            else:
                # Try to parse input time using various formats
                formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%dT%H:%M:%SZ', 
                           '%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%d %H:%M:%S%z', '%Y-%m-%d %H:%M:%S.%f%z', 
                           '%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%dT%H:%M:%S%zZ', '%Y-%m-%dT%H:%M:%S.%f%z']

                for format in formats:
                    try:
                        return datetime.strptime(input_time, format).astimezone(timezone.utc)
                    except ValueError:
                        continue
                
                # If unable to parse, raise an error
                raise ValueError("Invalid input format!")
            
        except Exception as e:
            print("Error:", e)
            sys.exit(1)
