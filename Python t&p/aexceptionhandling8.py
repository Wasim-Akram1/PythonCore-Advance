'''try:
    print("Outer try")
    try:
        print("inner try")
        print(10/0)
    except ZeroDivisionError:
        print(20/0)
        print("Inner Except")
    finally:
        print("Inner Finally")
except:
    print("Outer Except")
finally:
    print("Outer Finally")'''
try:
    print("1")
    print("2")
    print("3")
    try:
        print("4")
        print("5")
        print("6")
    except:
        print("7")
    finally:
        print("8")
    print("9")
except:
    print("10")
finally:
    print(10/0)
print("12")

#No Exception:- 1,2,3,4,5,6,8,9,11,12
#Exception at 2 except match:-1,10,11,12
#Exception at 2 except not match:-1,11,at
#Exception at 5 inner except matched:-1,2,3,4,7,8,9,11,12
#Exception at 5 inner except not matched but outer except matched:-1,2,3,4,8,10,11,12
#Exception at 5 but inner and outer both doesnt matched:-1,2,3,4,8,11,at
#Exception at 7 but except matched:-1,2,3,4,8,10,11,12
#Exception at 7 but except not matched:-1,2,3,4,8,11
#Exception at 8 but except matched:-1,2,3,4,5,6,10,11,12
#Exception at 8 but except not matched:-1,2,3,4,5,6,11,at
#Exception at 9 but except matched:-1,2,3,4,5,6,8,10,11,12
#Exception at 8 but except not matched:-1,2,3,4,5,6,8,11,at
#Exception at 10:-1,11
#Exception at 11:-1,2,3,4,5,6,8,9,at
