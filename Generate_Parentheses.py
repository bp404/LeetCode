#coding:utf-8 # 强制使用utf-8编码格式

class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		bp1 = []
		bp2 = []
		bp3 = []
		bp4 = []
		list = []
		for x in xrange(0,2*n):
			for y in xrange(0,2**x):
				if y%2 == 0:
					bp1.append(1)
				else :
					bp1.append(-1)
			bp2.append(bp1)
			# print bp1
			bp1 = []

		bp = 2*n-1
		for x in xrange(0,2**bp):
			# print x
			for b in xrange(0,2*n):
				bp3.append(bp2[bp-b][x/(2**b)])
			# list反向排序
			bp4.append(bp3[::-1])
			# print bp3[::-1]
			bp3 = []

		# print bp4

		for x in xrange(0,len(bp4)):
			sumbp = 0
			# print bp4[x]
			for y in xrange(0,2*n):
				sumbp = sumbp + bp4[x][y]
				if sumbp < 0:
					sumbp = 999
					break
			# print sumbp
			if sumbp == 0:
				# print bp4[x],sumbp
				list.append(bp4[x])
		for x in xrange(0,len(list)):
			for y in xrange(0,2*n):
				if list[x][y] == 1:
					list[x][y] = "("
				else :
					list[x][y] = ")"
		re = []
		for x in xrange(0,len(list)):
			# print list[x]
			s = ''.join(list[x])
			re.append(s)
			# print s
			# s = ''
		return re


bp = Solution()
print bp.generateParenthesis(4)
