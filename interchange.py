'''

Python program to interchange first and last elements in a list
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]
'''
def interchange(in_list):
    
    in_list[0],in_list[-1] = in_list[-1],in_list[0]
    return in_list

'''

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]
'''

def change_pos(inlist,pos1,pos2):
    inlist[pos1 - 1],inlist[pos2 - 1] = inlist[pos2 - 1],inlist[pos1 - 1]
    return inlist

def does_exist(inlist,num):
    if num in inlist:
        return num

list1 = [10,11,33,43,455,44,56]
print(interchange(list1))
print(change_pos(list1,2,4))
print(does_exist(list1,10))