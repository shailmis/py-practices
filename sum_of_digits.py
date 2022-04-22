'''

Sum of number digits in List
The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]
'''
def digits_sum(lst):
    sum_list = []
    for num in lst:
        sum_of_digits = 0
        for digit in str(num):
            #print(f'Single Digit is {digit}')
            sum_of_digits = sum_of_digits + int(digit)
        sum_list.append(sum_of_digits)
    return sum_list            

lst = [12, 67, 98, 34]
print(f' return value from function is {digits_sum(lst)}')
