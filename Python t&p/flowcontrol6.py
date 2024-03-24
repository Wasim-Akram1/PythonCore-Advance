s=input("Enter a string:-")
x=input("Enter a character to search:-")
'''flag=0
for i in s:
    if i==x:
        print("Found")
        flag=1
        break
if flag==0:
    print("Not Found")'''
if x in s:
    print("found")
else:
    print("Not found")