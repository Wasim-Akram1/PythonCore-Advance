def f1():
    try:
        return 10
    except:
        print("Exception")
    finally:
        print("Finally")
x=f1()
print(x)
