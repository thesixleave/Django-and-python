a=[[0]*3 for x in range(3)]
b=[[0]*3 for x in range(3)]
c=[[0]*3 for x in range(3)]
for x in range(len(a)):
    for y in range(len(a[x])):
        a[x][y]=int(input(''))

for x in range(3):
    for y in range(3):
        b[x][y]=int(input(''))
        c[x][y]=a[x][y]+b[x][y]
        
print(c)