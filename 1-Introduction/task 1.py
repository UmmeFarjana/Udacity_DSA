TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
count = 0
storage = set()
for i in range(0,len(calls)):   
        storage.add(calls[i][0])
        storage.add(calls[i][1])
for i in range(0,len(texts)):
        storage.add(texts[i][0])
        storage.add(texts[i][1])
print(f"There are {len(storage)} different telephone numbers in the records.")
