'''s=input("Enter a string:-")
sub=input("Enter a sub string:-")
count=0
x=-1
while True:
    x=s.find(sub,x+1,len(s))
    if x==-1:
        break
    count=count+1
print(count)

print(s.count(sub,3,9))

s1=s.replace("a","z")
print(s1)

l=s.split("-",2)
print(l)'''

l=eval(input("Enter a list:-"))
s="-".join(l)
print(s)

