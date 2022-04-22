'''
Given a list, print the value obtained after multiplying all numbers in a list. 
Examples: 
 

Input :  list1 = [1, 2, 3] 
Output : 6 
Explanation: 1*2*3=6 
'''
def multiply_items(lst):
    output = 1
    for item in lst:
        output = int(item) * output
    return output

list1 = [2,4,5]
print(f'multiplication of items in {list1} is {multiply_items(list1)}')