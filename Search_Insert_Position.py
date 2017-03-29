#coding:utf-8 # 强制使用utf-8编码格式

class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		# for x in xrange(0,len(nums)):
		# 	print nums[x]
		flag = -1
		num = -1
		for x in xrange(0,len(nums)):
			# print nums[x],"-",target,(nums[x] == target)
			if nums[x] == target:
				flag = 1
				num = num+1
			if nums[x] < target:
				flag = 0
				num = num+1
		bp0 = nums[0]
		if target < bp0:
			return 0
		if flag == 1:
		 	return num
		else :
			return num+1

list = [1,2,3,4,5];
bp = Solution()
print bp.searchInsert(list,2)
