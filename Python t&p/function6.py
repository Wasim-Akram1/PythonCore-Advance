'''def fact(n):
    if n==0:
        res=1
    else:
        res=n*fact(n-1)
    return res
x=fact(5)
print(x)

s=lambda x,y:x if x>y else y
print(s(2,4))
print(s(5,99))'''

l=[10,20,30,40,4,3,2,1,5,88,77,99]
l2=list(filter(lambda x:x%2!=0,l))
print(l2)
