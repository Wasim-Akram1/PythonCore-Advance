import os
try:
    print("I am Try")
    os._exit(0)
except:
    print("Except")
finally:
    print("finally")
