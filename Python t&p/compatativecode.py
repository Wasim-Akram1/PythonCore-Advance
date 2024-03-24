#Program to display the type of character entered(LCA, UCA,D S,SP)
'''t=int(input())
while t>0:
    s=input("Enter ba Character:- ")
    if s.isalnum():
        if s.isalpha():
            if s.islower():
                print("LCA")
            else:
                print("UCA")
        else:
            print("D")
    elif s.isspace():
        print("s")
    else:
        print("SP")
    t=t-1

#Program to reverse the character eg:- Wasim Akram = Akram Wasim
t=int(input("Enter number of test cases:-"))
while t>0:
    s=input("Enter a string:- ")
    l=s.split()
    x=-1
    while x>=-len(l):
        print(l[x],end=" ")
        x=x-1
    print()
    print()
    t=t-1'''

s=input("Enter a string:-")
'''s=s[::-1]
print(s)

x=-1
while x>=-len(s):
    print(s[x],end=" ")
    x=x-1'''
s1="".join(reversed(s))
print(s1)
                    
