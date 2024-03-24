#one two three four five
#one owt three ruof five

t=int(input())
while t>0:
    s=input()
    l=s.split()
    i=0
    while i<len(l):
        if i%2==0:
            print(l[i],end=" ")
        else:
            r=l[i]
            print(r[::-1],end=" ")
        i=i+1
    t=t-1
