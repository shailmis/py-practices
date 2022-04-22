'''
Given a list in Python and a number x, count number of occurrences of x in the given list.
Examples: 
 

Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
         x = 10
Output : 3 
10 appears three times in given list.
'''

def occurance(list,search_item):
    occured_times = 0
    for item in list:
        if item == search_item:
            occured_times = occured_times + 1
    return occured_times

lst = [15, 6, 7, 12, 12, 20, 12, 12, 10]
search_item = 12
print(f' {search_item} occured {occurance(lst,search_item)} times in {lst}')
# Another cleaner approach will be to invoke list.count
print(f' {search_item} occured {lst.count(search_item)} times in {lst}')