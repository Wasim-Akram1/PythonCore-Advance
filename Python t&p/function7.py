from functools import reduce
#from operator import *
l=[1,2,3,4,5,56,777,777]
'''l2=[10,20,30]
l3=list(map(lambda x,y:x*y,l,l2))
print(l3)

res=reduce(mul,l)
print(res)'''

res=reduce(lambda x,y:x if x>y else y,l)
print(res)


