a=10
b=20
def f1():
    global a
    a=20
   # print(a)
'''def f2():
    global a 
    a=a+50
    print(a)'''
print(globals()["a"])
f1()
print(type(globals()))
print(globals())
#f2()
