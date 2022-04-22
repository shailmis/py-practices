'''
Hourly log frequency

'''

from collections import defaultdict
import pprint
from collections import Counter

output = defaultdict(list)
log_freq = []

with open("syslog.log") as f:
    lines = f.readlines()
for line in lines:
    line = line.strip()
    line_list = line.split(' ')
    log_hour = line_list[3].split(':')[0]
    hostname = line_list[4]
    log_date_hour = f'{line_list[0]} {line_list[2]} {log_hour}'
    log_freq.append(log_date_hour)
freq = Counter(log_freq)
print(type(freq))
