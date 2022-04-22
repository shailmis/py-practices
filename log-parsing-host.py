'''
Write a script which parses /var/log/messages and generates a CSV with two columns: minute, number_of_messages
Sample log line 
Jan 20 03:25:08 fakehost logrotate: ALERT exited abnormally with [1]
'''
from collections import Counter
import csv
import json

output = []

fields = ["Date","Frequency"]
with open("messages.log") as f:
    lines = f.readlines()
for line in lines:
    line = line.strip()
    line_parts = line.split('fakehost')
    output.append(line_parts[0][:12])

print_count = Counter(output)
dict_out = dict(print_count)

with open("logs_output.csv","w") as f:
    f.write(json.dumps(dict_out))
