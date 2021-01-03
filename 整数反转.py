

class Solution():
    def invnum(self,inputs):
        str1=str(inputs)
        if str1[0]=='-':
            x=int(str1[:0:-1])
            print(x)
            x=-x
            return x if -21**31<x<21**31 else 0
        else:
            x=int(str1[::-1])
            print(x)
            return x if -21**31<x<21**31 else 0
inputs=-12321464894
tample1=Solution()
result=tample1.invnum(inputs)
print(result)

