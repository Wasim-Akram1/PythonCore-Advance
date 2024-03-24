t=int(input())
while t>0:
    s=input()
    alpha=""
    digit=""
    for i in s:
        if i.isalpha()==True:
            alpha=alpha+i
        if i.isdigit()==True:
            digit=digit+i
    for i in sorted(alpha):
        print(i,end="")
    for i in sorted(digit):
        print(i,end="")
    print()
    t=t-1
