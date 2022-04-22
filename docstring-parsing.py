import pprint

data = '''
UP,Lucknow
MP,Bhopal
Karnataka,Bangalore
Tamilnadu,Chennai
AP,Hyderabad
'''
character_count = {}

for char1 in data:
    #print (f'{char1}')
    character_count.setdefault(char1,0)
    character_count[char1] = character_count[char1] + 1

pprint.pprint(character_count)