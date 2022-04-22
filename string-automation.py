txt = '''
AFTER THE CLOSE OF THE SECOND QUARTER, OUR COMPANY,
CASTAÑACORP
... HAS ACHIEVED A GROWTH IN THE REVENUE OF 7.47%. THIS IS IN
LINE
... 
'''
#print(INPUT_TEXT)

words = txt.split()
redacted = []
print(f'{type(words)} {type(txt)}')
for word in words:
    if word.isdigit():
        redacted.append(''.join('X'))
    else:
        redacted.append(word)

print(redacted)

