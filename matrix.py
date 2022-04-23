'''
Initilize and print matrix

'''
import pprint

matrix = []

row = int(input("Enter  number of rows"))
col = int(input("Enter number of cols"))
mat_row = []
for r in range(row):
    mat_row = []
    for c in range(col):
        k = int(input())
        mat_row.append(k)
    matrix.append(mat_row)

#pprint.pprint(matrix)
#print(matrix)

for i in matrix:
    print(i)
     