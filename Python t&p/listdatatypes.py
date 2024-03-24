#List Data Types
'''l=[10,20,30]
print(l)
l=list(map(input().split()))
print(l)

s="Wasim Akram is a good boy"
l=s.split()
print(l)

l=[10,20,30,40,50,60,70,10,10,30]
l1=[80,90]
#print(l[::2])
for i in l:
    print(i)
i=0
while i<len(l):
    print(l[i])
    i=i+1
print(len(l))
x=l.count(10)
print(x)

x=l.index(10)
print(x)
l.append(10)
print(l)

l.insert(-999,100)
l.insert(999,1000)
print(l)

l.extend(l1)
print(l)

l.remove(10)
l.remove(10)
l.pop(3)
l.reverse()
l.sort()
l.sort(reverse=True)
print(l)

l1=[10,20,30]
l2=l1[::1]
print(id(l1))
print(id(l2))
l2[1]=(100)
print(l1)
print(l2)'''

l1=[10,20,30]
l2=[40,50,60,[7,80]]
print(l1+l2)
print(l1*3)
print(l1==l2)
print(10 in l1)
l1.clear()
print(l1)
print(l2[0])
print(l2[1])
print(l2[2])
print(l2[3])
print(l2[3][0])
print(l2[3][1])
