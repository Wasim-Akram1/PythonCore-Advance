#program to find no of times a char occurred
t=int(input())
while t>0:
    s=input()
    '''l=[]
    for i in s:
        if i not in l:
            l.append(i)
    for i in l:
        j=0
        count=0
        while j<len(s):
            if s[j]==i:
                count=count+1
            j=j+1
        print(i,"occurred",count,"times")
    t=t-1'''

    d={}
    for i in s:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]=d[i]+1
    for k,v in d.items():
        print(k,"occurred",v,"times")
    t=t-1
