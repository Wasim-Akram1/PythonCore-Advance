def calculator(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
a=int(input("Enter the first number:-"))
b=int(input("Enter the second number:-"))
#s,su,m,d=calculator(a,b)
t=calculator(a,b)
print(type(t))
for i in t:
    print(i)
'''print("sum is",s)
print("sub is",su)
print("mul is",m)
print("div is",d)'''
