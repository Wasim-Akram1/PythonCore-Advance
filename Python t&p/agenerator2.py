'''def countdown(n):
    while n>=1:
        yield n
        n=n-1
n=int(input())
g=countdown(n)
for i in g:
    print(i)'''

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
g=fib()
for i in g:
    if i<1000:
        print(i,end="-")
    else:
        break
