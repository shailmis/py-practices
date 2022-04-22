'''
This is the first program to create a class for a student having following attibutes:
Name , Age
'''
class Student:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

student1 = Student("shailesh",45)

print(student1.name)

class Boy:
    def __init__(self) -> None:
        pass

name2 = [
    "hello",
    "hi",
    "testing",
]