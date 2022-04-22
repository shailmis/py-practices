'''
Given a list of numbers, the task is to write a Python program to find the smallest number in given list.
Examples: 

Input : list1 = [10, 20, 4]
Output : 4
'''
def smallest_num(lst):
    smallest_number = 0
    for item in lst:
        if int(item) < smallest_number:
            smallest_number = int(item)
    return smallest_number

list1 = [10,11,3,4,343,0,-1]
print(f'Smallest number among {list1} is {smallest_num(list1)}')