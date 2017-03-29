#coding:utf-8 # 强制使用utf-8编码格式

class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		bp1 = []
		bp2 = []
		sumnum = 0
		count = len(nums)
		for x in xrange(0,len(nums)):
			sumnum = sumnum + nums[x]
		
		for x in xrange(0,len(nums)+1):
			for y in xrange(0,count**x):
				bp1.append(nums[y%count])
			bp2.append(bp1)
			bp1 = []
		# for x in xrange(0,len(bp2)):
		# 	print bp2[x]
		
		bp3 = []
		bp4 = []
		# print len(nums)
		for x in xrange(0,count**count):
			for y in xrange(0,len(nums)):
				bp3.append(bp2[count-y][x/(count**y)])
			bp4.append(bp3)
			bp3 = []
			
			# bp4.append(bp3)
			# bp3 = []
		list1 = []
		list2 = []
		numtest = 0
		for x in xrange(0,len(bp4)):
			for y in xrange(0,count):
				numtest = numtest + bp4[x][y]
			if numtest == sumnum:
				list1.append(bp4[x])
			numtest = 0
		list = []
		for x in xrange(0,len(list1)):
			if len(list1[x]) == len(set(list1[x])):
				list.append(list1[x])
		bp404 = []
		for x in xrange(0,len(list)):
			bp404.append(list[x][::-1])
		return bp404


list = [1,2,3]
bp = Solution()
print bp.permute(list)
