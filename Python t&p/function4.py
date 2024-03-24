def sum(*t,name):
    '''print(type(t))
    sum=0
    for i in t:
        sum=sum+i
    print(sum)
sum(10,20)
sum(10,20,300)
sum()
sum(10,10,200,299,29999,88765,43232)

    sum=0
    for i in t:
        sum+=i
    print(name,"your total marks are",sum)
sum(10,20,30,40,50,name="Wasim")'''

def student(**d):
    print(type(d))
    for k,v in d.items():
        print(k,"->",v)
student(name="Wasim Akram", Age=22, weight=65, height=167)
student(gf="Sama", ex="Sufiya")
