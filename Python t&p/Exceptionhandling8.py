class OldException(Exception):
    def __init__(self,arg):
        self.msg=arg
class YpungException(Exception):
    def __init__(self,arg):
        self.msg=arg
a=int(input())
if a>60:
    raise OldException("Buddha Ho gaya sadi krega hahaha")
elif a<18:
    raise YpungException("Pehle jawan ho ja")
else:
    print("Matching")

