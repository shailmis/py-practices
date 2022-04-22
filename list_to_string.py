'''

Convert list of comma seperated string

'''
names = [
    "Shailesh",
    "Shivansh",
    "Saatvik",
    "Kamalini"
]
str_names = ""
str_names = ','.join(str(name) for name in names)
str_names1 = ','.join(names)
print(str_names1)

big_string = "this is the big string which we wish to convert into list"
str_list = big_string.split(' ')
print( type(str_list))
list1 = ' '.join([names[1], names[2]])
print(type(list1))


