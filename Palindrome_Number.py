#coding:utf-8 # 强制使用utf-8编码格式

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False
        else :
        	numlen = len("%d"%x)
	        num = 0
	        list = []
	        for i in xrange(1,numlen+1):
	        	list.append(x % 10)
	        	x = x / 10
	    	# print list
	    	num = 0
	    	for i in xrange(1,numlen+1):
	    		if list[i-1] == list[numlen-i]:
	    			num = num + 1
	    	if num == numlen:
	    		return True
	    	else :
	    		return False
bp = Solution()
print bp.isPalindrome(-12321)