from datetime import datetime
import time

input_time = 1730106636
time_format = "%d-%m-%Y %H:%M:%S"

if __name__ == "__main__":
    current_time_unix = time.time()
    current_time = datetime.fromtimestamp(current_time_unix).strftime(time_format)
    print("Current time: ",current_time)

    local_time = datetime.fromtimestamp(input_time).strftime(time_format)

    print("Input timestamp: ", input_time, " Result: ", local_time)