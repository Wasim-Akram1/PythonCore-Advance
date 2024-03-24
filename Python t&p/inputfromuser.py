'''x=int(input("Enter first number:- "))
y=int(input("Enter second number:-"))
print("Sum is:-",(x+y))

print("sum is:- ",(int(input("Enter first number"))+(int(input("Enter Second number")))))

#Program to swap 2 variable with the help of third variable
a=int(input("Enter any number:- "))
b=int(input("Enter any number:- "))
c=a
a=b
b=c
print("a value is",a,"b value is ",b)'''

#Program to swap 2 variable without the help of third variable
a=int(input("Enter a number:- "))
b=int(input("Enter second number:-"))
a=a+b
b=a-b
a=a-b
print("First nymber is ",a)
print("Second number is ",b)