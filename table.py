'''
table for 1 to 10

'''
for row in range(1,11):
    print(f'Table of {row}')
    for col in range(1,11):
        print(f'{row} X {col} = {row*col}')
