import logging
logging.basicConfig(filename="log1.text", level=logging.ERROR)
print("Procerss Successfully Started")
try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("cant divide by zero")
    logging.exception(e)
except ValueError as e:
    print("Take Integer only")
    logging.exception(e)
print("Process Completed")
