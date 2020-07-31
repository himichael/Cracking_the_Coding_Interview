class Solution(object):
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        n = len(nums)
        for i in xrange(n):
            if i==nums[i]:
                return i
        return -1
		
		
		
	# 二分查找
    def findMagicIndex(self, nums):
        if not nums:
            return -1
        def dfs(begin,end):
            if begin>end:
                return -1
            mid = begin+(end-begin)//2
            left = dfs(begin,mid-1)
            if left!=-1:
                return left
            elif nums[mid]==mid:
                return mid
            return dfs(mid+1,end)
        return dfs(0,len(nums)-1)