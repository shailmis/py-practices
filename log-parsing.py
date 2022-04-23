'''
Write a script which parses /var/log/messages and generates a CSV with two columns: minute, number_of_messages
Sample log line 
Jan 20 03:25:08 fakehost logrotate: ALERT exited abnormally with [1]
'''
from collections import Counter
import pprint

output = []
with open("messages.log") as f:
    lines = f.readlines()
    
for line in lines:
    line = line.strip()
    tokens = line.split(" ")
    minutes = f'{tokens[2].split(":")[0]} {tokens[2].split(":")[1]}'
    #print(minutes)
    date_time = f'{tokens[0]} {tokens[1]} {minutes}'
    output.append(date_time)

#print(Counter(output))
final_print = Counter(output)

for item in final_print.elements():
    print(f'{item} {final_print[item]}')
    