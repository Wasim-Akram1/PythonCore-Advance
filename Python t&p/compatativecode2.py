#Wasim Akram loves Python = misaW markA sevoL nohtyP
t=int(input())
while t>0:
    s=input("Enter a character:-")
    l=s.split()
    for i in l:
        print(i[::-1],end=" ")
    t=t-1
        
