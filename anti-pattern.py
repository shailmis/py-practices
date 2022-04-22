'''

1. Not using items() to iterate over a dictionary

'''

countries = {
    "IN": "India",
    "PK": "Pakistan",
    "US": "United States",
    "BD": "Bangla Desh"
}
# Bad Practice
for code in countries:
    print(f'{countries[code]}')

# Good practice
for code, country in countries.items():
    print(f'{country}')
    print(type(code))

'''
2. Not using get() to return default values from a dictionary
'''

# Bad practice
if "IN" in countries:
    country_name = countries["IN"]
else:
    country_name = "Undefined"

# Good practice
country_name = countries.get("IN","Undefined")

'''

3. Not using enumerate when you need item and index at the same time
'''

fruits = [
    "Apple",
    "Mango",
    "Cheeku",
    "Oranges",
    "Banana"
]

# Bad practice
for i in range(len(fruits)):
    print(f'Fruit placed at {i+1} is {fruits[i]}')

# Good Practice
for i, fruit in enumerate(fruits):
    print(f'Fruit placed at {i+1} is {fruit}')
    