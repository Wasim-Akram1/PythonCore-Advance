def f1():
    try:
        return 123
    #except:
    except ZeroDivisionError:
        return 321
    finally:
        return 619
x=f1()
print(x)
