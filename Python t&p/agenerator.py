'''l=(i*i for i in range(1000000))
print(type(l))
print(next(l))
print(next(l))
print(next(l))
for i in l:
    print(i)'''

#Yield Keyword
def mygenerator():
    print("I am Generator")
    yield "A"
    yield "B"
    yield "C"
g=mygenerator()
for i in g:
    print(i)
