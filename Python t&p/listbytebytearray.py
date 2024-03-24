l=[10,20,30,40,50]
print(l)
for i in l:
    print(i)
l.append(60)
print(l)
l=["Wasim",10,10.5]
print(l)
l=[10,20,30]
print(l*3)
l=["Wasim"]
print(l*3)
l=[10,20,30,40]
b=bytes(l)
for i in b:
    print(i)
print(b[0])
#print(b[10])
l={10,20,600}
#b=bytes(l)
#print(b)
l=[10,20,30,40,50,60,70]
b=bytearray(l)
for i in b:
    print(i)
b[0]=90
for i in b:
    print(i)
#b[0]=900