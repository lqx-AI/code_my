class Solution():
    def distance(self,x,y):
        count=0
        x,y=bin(x),bin(y)
        print('zheli',x,y)
        m,n=len(x[2:]),len(y[2:])
        print('here',m,n)
        for i in range(m):        #i 和j都为字符串需要转话成整型
            for j in range(n):
                if x[i]==y[j] and i!=j:
                    print(i,j)
                    count+=1
                else:
                    continue
        return count
x,y=1,4
test=Solution()
result=test.distance(x,y)
print(result)


#-----------------------------------------------
class Solution:
    def hammingDistance(self, x, y):
        xor = x ^ y
        print(xor)
        distance = 0
        while xor:
            distance += 1
            # remove the rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance
x,y=1,4
test=Solution()
result=test.hammingDistance(x,y)
print(result)



