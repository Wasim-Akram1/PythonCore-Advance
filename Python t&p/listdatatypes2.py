'''l=[i*2 for i in range(10)if i%2==0]
print(l)

l=["Bhopal","Mubai","Indore","Delhi"]
l2=[i[0] for i in l]
print(l2)

l=[10,20,30]
l2=[30,20]
l3=[i for i in l if i in l2]
print(l3)

s="The Quick Brown fox jump over the lazy dog "
l=s.split()
l2=[[i, len(i)] for i in l]
print(l2)'''

s=input()
s=s.lower()
v=['a','e','i','o','u']
found=[ ]
for i in s:
    if i in v:
        if i not in found:
            found.append(i)
s2="".join(found)
print(s2)
