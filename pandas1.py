import pandas as pd
import re
import json

files_dict = {}
with open("accesslog.log") as f:
    lines = f.readlines()
logs = pd.DataFrame( {'ip': [], 'time': [], 'request': [], 'status': [],'size': [], 'Referer': [], 'User_agent': []} )
regc = re.compile('(?P<ip>.*?) - - \[(?P<time>.*?)\] "(?P<request>.*?)" (?P<status>\d+) (?P<size>\d+) (?P<Referer>.*?) (?P<User_agent>.*?)')

for line in lines:
    m = regc.match(line)
    print(m)
    ip = m.group('ip')
    #identd = m.group('identd')
    #userid = m.group('userid')
    time = m.group('time')
    request = m.group('request')
    status = m.group('status')
    size = m.group('size')
    Referer = m.group('Referer')
    User_agent = m.group('User_agent')
    #logs.append([ip,time, request, status, size, Referer, User_agent], ignore_index=False)
    files_dict = {'ip':ip, 'time': time, 'request': request, 'status':status, 'size': size, 'Referer': Referer, 'User_agent':User_agent }
    
print(files_dict)