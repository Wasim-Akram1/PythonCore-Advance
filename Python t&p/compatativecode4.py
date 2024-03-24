t=int(input())
while t>0:
    s1=input()
    s2=input()
    s3=""
    i=0
    j=0
    while i<len(s1) or j<len(s2):
        if i<len(s1):
            s3=s3+s1[i]
            i=i+1
        if j<len(s2):
            s3=s3+s2[j]
            j=j+1
    print(s3)
    print()
    i=i-1
