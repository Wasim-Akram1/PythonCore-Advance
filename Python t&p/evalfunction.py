'''x=eval(input("Enter something:-"))
print(type(x))'''

x=eval(input("Enter first number:-"))
y=eval(input("Enter Second Number:-"))
z=eval(input("Enter the third number:- "))
greatest=x if x>y and x>z else y if y>x and y>z else z
print("Greatest number is:-",greatest)