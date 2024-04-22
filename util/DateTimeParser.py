import sys
import re
from datetime import datetime, timezone, timedelta

class DateTimeParser:

    @staticmethod
    def parse_input(input_time):
        try:
            pattern = r'\b\d+\b'

            # Try to parse input time as an integer (epoch time)
            if input_time.lower() == "now":
                return datetime.now(timezone.utc)
            
            elif input_time.lower().startswith("add"):

                integer = int(re.search(pattern, input_time).group())
                

                if input_time.lower().endswith("days"):
                    time = datetime.now(timezone.utc) + timedelta(days=integer)
                if input_time.lower().endswith("minutes"):
                    time = datetime.now(timezone.utc) + timedelta(minutes=integer)
                if input_time.lower().endswith("hours"):
                    time = datetime.now(timezone.utc) + timedelta(hours=integer)
                return time

            elif input_time.lower().startswith("subtract"):

                integer = int(re.search(pattern, input_time).group())

                if input_time.lower().endswith("days"):
                    time = datetime.now(timezone.utc) + timedelta(days=-integer)
                if input_time.lower().endswith("minutes"):
                    time = datetime.now(timezone.utc) + timedelta(minutes=-integer)
                if input_time.lower().endswith("hours"):
                    time = datetime.now(timezone.utc) + timedelta(hours=-integer)
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
