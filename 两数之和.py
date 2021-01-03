class Solution:
	def twoSum(self,nums,target):
		n = len(nums)
		for x in range(n):
			a = target - nums[x]
			if a in nums: # 判断a有没有在nums数组里
				y = nums.index(a) # 有的话，那么用index获取到该数字的下标
				if x == y:
					continue # 同样的数字不能重复用，所以这里如果是一样的数字，那么就不满足条件，跳过
				else: # 否则就返回结果
					return x,y
					break
			else:
				continue # 上面的条件都不满足就跳过，进行下一次循环


nums = [2, 7, 11, 16]
target = 9
result=Solution()
print(result.twoSum(nums,target))


def twoSum(self, nums, target):
	d = {}
	n = len(nums)
	for x in range(n):
		if target - nums[x] in d:
			return d[target - nums[x]], x
		else:
			d[nums[x]] = x
