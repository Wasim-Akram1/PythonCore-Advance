a=int(input())
b=int(input())
try:
    c=a/b
    print(c)
except ZeroDivisionError as x:
    print(f"{x} is the error")
