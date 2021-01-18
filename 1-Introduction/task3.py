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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls 
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# Part A
target_prefix = set()
for i in range (0, len(calls)):
    if calls[i][0].startswith("(080)"):
        calling = calls[i][1]
        if calling.startswith("140"):
            target_prefix.add("140")
        if ' ' in calling and calling.startswith(("7","8","9")):
            target_prefix.add(calling[0:4])
        if calling.startswith("(0"):
            my_split = calling.split(")")
            target_prefix.add(my_split[0]+ ")")
print(f"The numbers called by people in Bangalore have codes: ")
print(*sorted(target_prefix), sep='\n')


# Part B
count_b2b = 0 # Bangalore to Bangalore calls
count_b2a = 0 # Bangalore to other places calls
for i in range (0, len(calls)):
    if calls[i][0].startswith("(080)"):
        if calls[i][1].startswith("(080)"):
            count_b2b += 1
        else:
            count_b2a += 1
percentage_b2b = count_b2b / (count_b2b + count_b2a)* 100
print(f"{percentage_b2b:.2f} percent of calls from fixed lines in Bangalore are calls"
      f" to other fixed lines in Bangalore.")



