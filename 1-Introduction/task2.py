"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

counter = {}
for i in range (len(calls)):
    caller = calls[i][0]
    receiver = calls[i][1]
    time = int(calls[i][3])
    if caller in counter:
        counter[caller] += time
    else:
        counter[caller] = time
    if receiver in counter:
        counter[receiver] += time
    else:
        counter[receiver] = time
max_time = 0
for number in counter:
    time = counter[number]
    if time> max_time:
        max_time = time
        max_time_num = number
print(f"{max_time_num} "
      f"spent the longest time, {max_time} seconds, "
      f"on the phone during September 2016.")
