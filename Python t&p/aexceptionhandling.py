print("Lets Begin")
a=int(input("Enter a number:-"))
b=int(input("Enter a number:- "))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Cannot divide ")
print("Rest of the program")
