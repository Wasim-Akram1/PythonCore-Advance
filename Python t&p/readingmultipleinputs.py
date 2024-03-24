'''a,b,c=[eval(x)for x in input("Enter Number:-").split("_")]
print(a,b,c)'''
a,b=[eval(x)for x in input("Enter two number:-").split()]
ans=1 if a==b else 0
print(ans)
