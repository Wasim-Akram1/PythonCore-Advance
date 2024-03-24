#program to print string character alternatively 
t=int(input())
while t>0:
    s=input()
    '''print(s[::2])
    print(s[1::2])
    t=t-1'''

    i=0
    while i<len(s):
        print(s[i],end="")
        i=i+2
    print()
    i=1
    while i<len(s):
        print(s[i],end="")
        i=i+2
    print()
    t=t-1
