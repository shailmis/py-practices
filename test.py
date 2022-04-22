'''
Multi line comment
Lets see
'''
courses = ["Art","Science","Hindi","English"]
print(f'Courses offered are {courses[0]},{courses[1]},{courses[2]},{courses[-1]}')
#print(dir(courses))
"append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']"
courses.append("CompSci")
second_courses_list = courses.copy()
print(second_courses_list)
print(type(second_courses_list))

a = "first"
b = "first"


# Returns the actual location
# where the variable is stored
print(id(a))

# Returns the actual location
# where the variable is stored
print(id(b))

# Returns true if both the variables
# are stored in same location
print(a is b)

def fun1():
    lst = dict(10,11,23,34,34,55)
    return lst
print(type(fun1()))