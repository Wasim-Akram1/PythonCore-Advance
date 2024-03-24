n=eval(input("Enter the number of rows:-"))
'''for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end="")
    print()
for i in range(1,n+1):
    print("*"*n)
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,n+1):
    print("*"*i)
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end="")
    print()'''
i=1
for i in range(i,n+2-i):
    print("*"*n)