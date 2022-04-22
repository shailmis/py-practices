'''
Write a program which prints out all numbers between 1 and 100. 
When the program would print out a number exactly divisible by 4, 
print "Linked" instead. When it would print out a number exactly divisible by 6, print "In" instead. 
When it would print out a number exactly divisible by both 4 and 6, print "LinkedIn."
'''
num = []

for count in range(1,101):
    if count%4 == 0 and count%6 == 0 :
        num.append("LinkedIn")
    elif count%4 == 0:
        num.append("Linked")
    elif count%6 == 0:
        num.append("In")
    else:
        num.append(count)

print(num)
