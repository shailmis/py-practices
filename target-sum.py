'''

Target sum of integers
numbers = [ 10,11,34,54,55,6,4,5,3]
target = 11
return pair if sum of any two digits equals to target . Here it will be 6,5
'''
def find_target_sums(numbers,target):
    for pair1 in numbers:
        for pair2 in numbers:
            if pair1 + pair2 == target:
                print(f'First Number = {pair1} , Second Number = {pair2}')
                
numbers = [4,5,6,10,4,5,2,7]
numbers = list(set(numbers))
target = 9
find_target_sums(numbers,target)

