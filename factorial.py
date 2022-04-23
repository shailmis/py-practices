'''
Write a function fact to calculate factorial and call recursively

'''

def fact(num):
    '''
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)
    '''
    return 1 if num == 0 else num * fact(num - 1)

print(fact(5))
