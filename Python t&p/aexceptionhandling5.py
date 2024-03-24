'''try:
    #print("I am try")
    print(10/0)
#except Exception:
except ValueError as e:
    print("Except Block")
finally:
    print("finally")'''

try:
    print("Trying")
finally:
    print("Finally")
