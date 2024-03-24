'''def f1():
    print("Heloow")
f2=f1
f1()
f2()
print(id(f1))
print(id(f2))'''

def outer():
    print("Outer Running")
    def inner():
        print("inner running")
    print(id(inner)) 
    print("Outer ended")
    return inner
f1=outer()
print(id(f1))
f1()
        
