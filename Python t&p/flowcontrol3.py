'''i=1
while i<=100:
    print(i)
    i=i+2
n=int(input("How many numbers:-"))
l=eval(input("Enter the list of values"))
sum=0
i=0
while i<n:
    sum=sum+l[i]
    i=i+1
print(sum)
n=int(input("Enter the number:-"))
sum=0
while n>0:
    b=n%10
    sum=sum+b
    n=n//10
print("sum is",sum)'''
x=1
while x<=100:
    if x%7==0:
        print(x)
    x=x+1