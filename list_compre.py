'''
Write a program to calculate square of even numbers
'''
input_list = [10,12,18,17,3,4,6,33,56]
#new_list = []
new_list = [ n*n for n in input_list if n%2 == 0]
print(new_list)


'''
Write a program to print (number,char) for each letter in 'abcde' and '0123'

'''
mylist = []
for i in 'abcde':
    for j in range(4):
        mylist.append((i,j))
print(mylist)
mylist = [(char,num1) for char in 'abcde' for num1 in range(4)]
print(mylist)


'''
Write a function to create list of tuples of state and capital
'''

states = ["UP","MP","Delhi","Karnataka","Tamilnadu"]
capitals = ["Lucknow","Bhopal","New Delhi","Bangalore","chennai"]
states_capitals = zip(states,capitals)  # Zip function create list object of tuples from two different lists
print(list(states_capitals))


'''
Write a program to create dict my_dict{'state : 'capital'} for each of the tuple in zip(states,capitals)

'''
my_dict = {}
for state,capital in states_capitals:
    my_dict[state] = capital
print(my_dict)

my_dict = {state: capital for state,capital in zip(states,capitals) if state != 'UP'}
print(my_dict)
