t=int(input())
while t>0:
    s=input()
    '''alpha=""
    for i in s:
        if i.isalpha()==True:
            alpha=alpha+i
    j=1
    for i in alpha:
        print(i*int(s[j]),end="")
        j=j+2
    t=t-1'''
    for i in s:
        if i.isalpha()==True:
            print(i,end="")
            x=i
        if i.isdigit()==True:
            print(chr(ord(x)+int(i)),end="")
    t=t-1
    
