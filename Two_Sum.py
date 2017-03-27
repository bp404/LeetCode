#coding:utf-8 # 强制使用utf-8编码格式

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        y = 0
        x = 0
        for i in nums:
            for j in nums:
                if(x != y and i+j == target):
                    nums.index(i)
                    # print i,j
                    # print y,x
                    return [y,x]
                x = x+1
            y = y+1
            x = 0

list = [3,3]
bp = Solution()
print bp.twoSum(list,6)