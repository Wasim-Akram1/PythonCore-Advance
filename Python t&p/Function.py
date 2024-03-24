'''def wish(name):
    print("Happy Birthday",name)
x=10
y=20
z=x+y
print(z)
wish("Wali")
wish("Altaf")
wish("Aarif")
wish("Dilkash")

from math import pi
def area(r):
    ans=pi*r*r
    return ans
r=int(input("Enter the radius of a circle:-"))
catch=area(r)
print("The area of the circle is:",catch)
j=area(14)
print(j)

def evenodd(a):
    if a%2==0:
        print("Even")
    else:
        print("Odd")
evenodd(10)
evenodd(10999)
evenodd(101111)
evenodd(102)
evenodd(103)

def love(gf):
    print("I Love you so much",gf)
love("sama")
love("nazia")'''

from math import factorial
def fact(a):
    """Functions take a numer and return its factorial"""
    x=factorial(a)
    return x
a=int(input("Enter the number:- "))
catch=fact(a)
print("Factorial is: ",catch)
print(fact.__doc__)
    


