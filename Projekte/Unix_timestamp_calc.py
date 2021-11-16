from datetime import datetime
import time
import sys
import getopt

opts, rest = getopt.getopt(sys.argv[1:], "t:")

def get_date_time(timestamp):
    # if you encounter a "year is out of range" error the timestamp
    # may be in milliseconds, try `ts /= 1000` in that case
    return datetime.utcfromtimestamp(timestamp).strftime('%d.%m.%Y %H:%M.%S (UTC)')

for opt, arg in opts:
    if opt == '-t':
        insert_timestamp = arg
        print(get_date_time(int(insert_timestamp)))
        now = time.time()
        print(f"Aktueller timestamp: {now} ({get_date_time(now)})") #returns the unix timestamp

