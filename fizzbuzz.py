'''
Write a program which prints out all numbers between 1 and 100. 
When the program would print out a number exactly divisible by 4, 
print "Linked" instead. When it would print out a number exactly divisible by 6, print "In" instead. 
When it would print out a number exactly divisible by both 4 and 6, print "LinkedIn."
'''
for num in range(1,20):
    if num%4 == 0:
        print(f'Number {num} Linked')
    if num%6 == 0:
        print(f'Number {num} In')
    if num%4 == 0 and num%6 == 0:
        print(f' Number {num} Linkedin')
    
for number in range(1,20):
    if number%4 == 0 and number%6 == 0 :
        print(f' Number {number} Linkedin')
    elif number%6 ==0:
        print(f' Number {number} In')
    elif number%4 ==0:
        print(f'Number {number} Linked')

a = []
for i in range(1,101):
    if (i%4) == 0 and (i%6) == 0: # swap conditions wiht 9 and 13
       a.append("LinkedIn")
    elif (i%6) == 0:
        a.append("In")
    elif (i%4) == 0: # this line
        a.append("Linked")
    else:
       a.append(i)
print(a)
  