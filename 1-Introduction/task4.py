"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

calling = set()
receiving = set()
texting = set()

for i in range(0, len(calls)):
    calling.add(calls[i][0])
    receiving.add(calls[i][1])
    
for i in range(0, len(texts)):
    texting.add(texts[i][0])
    texting.add(texts[i][1])
    
print(f"These numbers could be telemarketers:")
telemarketers = []
for calling_num in calling:
    if calling_num not in receiving and calling_num not in texting:
        telemarketers.append(calling_num)
print(*sorted(telemarketers),sep='\n')
