from random import *
'''s="0123456789"
otp=""
for i in range(6):
    otp=otp+s[randint(0,9)]
print(otp)'''
for i in range(5):
    print(chr(randint(65,112)),randint(0,9),chr(randint(65,112)),randint(0,9),chr(randint(65,112)),randint(0,9),sep="")
