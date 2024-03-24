'''try:
    print(10/0)
#except ZeroDivisionError as e:
except ArithmeticError as e:
    #print(e)
    print(e.__class__.__name__)
    print(type(e).__name__)'''

try:
    a=int(input())
    b=int(input())
    c=a/b
except ZeroDivisionError as e:
    print(e)
except OverflowError as e:
    print("OverFlow")
except:
    print("I am default except block")
'''except(ValueError, ZeroDivisionError,BaseException) as e:
    print(e)
#except ZeroDivisionError as e:
except Exception as e:
    #print(e)
    print("Go")
except ValueError as e:
    print(e)
    print(type(e).__name__)'''
