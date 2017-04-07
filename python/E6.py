a=input('')
b=''
for x in range(0,len(a)):
    b=ord(chr(ord(a[x])))   
    if b>96 and b<122:
        b=b-32
        b=chr(b)
    elif b>47 and b<58:
        b='0'
        b=str(b)
    else:
        b=chr(b)

    print(end=b)

"""
ord()主要是用來返回ascii碼
chr()則是表示ascii碼對應的字
"""