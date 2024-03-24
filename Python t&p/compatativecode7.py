#Remvo duplicate character
t=int(input())
while t>0:
    s=input()
    '''l=[]
    for i in s:
        if i not in l:
            l.append(i)
    s1="".join(l)
    print(s1)
    t=t-1'''

    s1=set(s)
    s2="".join(s1)
    print(s2)
    t=t-1
