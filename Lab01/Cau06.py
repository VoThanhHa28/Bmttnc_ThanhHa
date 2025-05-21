x = int(input('Enter x: '))
y = int(input('Enter y: '))
dimensions=[x, y]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row*col
print(multilist)