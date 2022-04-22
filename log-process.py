'''
how many requests per IP address
file name = accesslog.log

42.236.10.125 - - [19/Dec/2020:15:23:10 +0100] "GET / HTTP/1.1" 200 10479 "http://baidu.com/" "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00 Build/HUAWEIEML-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 baidu.sogo.uc.UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN" "-"
'''

import re
from collections import Counter
import pprint
from collections import defaultdict

#myregex = r'\[(.*?)\]' to read all between []

ip_counts = []
datetime_list = []
file_content = defaultdict(list)
with open("accesslog.log") as f:
    lines = f.readlines()
for line in lines :
    line = line.strip()
    result = line.split(' ')
    log_ip = result[0]
    ip_counts.append(log_ip)
    date_time = result[3][1:15]
    if date_time in line:
        file_content[date_time].append(log_ip)

    datetime_list.append(date_time)
    #print(date_time)
    
#pprint.pprint(Counter(ip_counts))
#pprint.pprint(Counter(datetime_list))
pprint.pprint(file_content)
