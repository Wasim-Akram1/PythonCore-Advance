'''try:
    print("Try")
    print(10/0)
except:
    print("Except")
else:
    print("else")
finally:
    print("finally")

try:
    print("Hii")
except:
    print("go")
else:
    print("bye")
finally:
    print("toy")

try:
    print("try")
except ZeroDivisionError:
    print("except 1")
except ValueError:
    print("except 2")
except:
    print("Except 3")
else:
    print("else")
finally:
    print("Finally")

try:
    print("try")
except:
    print("Except")
try:
    print("Try2")
finally:
    print("finally")

try:
    print("hiio")
    try:
        print("iNNER try")
        print(10/0)
    except:
        print("Inner Except")
    else:
        print(10/0)
except:
    print("outer except")

try:
    print("try")
    print(10/0)
except:
    try:
        print("1")
    except:
        print("2")
    else:
        print("3")
    finally:
        print("4")'''

try:
    print("Hii")
except:
    print("bye")
else:
    print("else")
finally:
    print("finally")
