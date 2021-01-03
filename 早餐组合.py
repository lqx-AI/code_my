
class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        sum=0
        for i in staple :
            for j in drinks:
                if i+j<=x:
                    sum+=1#不用声明全局变量
                else:
                    continue #break不对
        return sum # 位置不同结果不一样

staple = [2,1,1]
drinks = [8,9,5,1]
x = 9
test=Solution()
result=test.breakfastNumber(staple,drinks,x)
print(result)


