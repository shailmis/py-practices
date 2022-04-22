'''
Reversing a List in Python
Input : list = [10, 11, 12, 13, 14, 15]
Output : [15, 14, 13, 12, 11, 10]
'''

import time

def reverse_list(in_list):
    in_list.reverse()
    return in_list

input_list = [10,33,23,43]
start_time = time.time()
print(reverse_list(input_list))
execution_time = str(time.time() - start_time)
print(f'Time take to execute this code is {execution_time}')