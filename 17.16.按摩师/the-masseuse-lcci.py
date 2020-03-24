class Solution(object):
	# 递归(超时)
	def massage(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		n = len(nums)
		def dfs(index,status):
			if index==n:
				return 0
			a,b,c = 0,0,0
			a = dfs(index+1,status)
			if status:
				b = dfs(index+1,False)+nums[index]
			else:
				c = dfs(index+1,True)
			return max(a,b,c)
		return dfs(0,True)
		
		
		
	# 递归+记忆化
	def massage(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		n = len(nums)
		mem = [[-1]*2 for _ in xrange(n)]
		def dfs(index,status):
			if index==n:
				return 0
			if mem[index][status]>-1:
				return mem[index][status]
			a,b,c = 0,0,0
			a = dfs(index+1,status)
			if status==1:
				b = dfs(index+1,0)
			else:
				c = dfs(index+1,1)+nums[index]
			mem[index][status] = max(a,b,c)
			return mem[index][status]
		return dfs(0,0)
		

		
	# 动态规划，一维数组
	def massage(self, nums):
		if not nums or len(nums)==0:
			return 0
		if len(nums)==1:
			return nums[0]
		n = len(nums)
		dp = [0 for _ in xrange(n)]
		dp[0] = nums[0]
		dp[1] = max(nums[0],nums[1])
		for i in xrange(2,n):
			dp[i] = max(dp[i-1],dp[i-2]+nums[i])
		return dp[-1]
		
		
		
	# 动态规划，O(1)空间
	def massage(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums or len(nums)==0:
			return 0
		if len(nums)==1:
			return nums[0]
		n = len(nums)
		dp0 = nums[0]
		dp1 = max(nums[0],nums[1])
		for i in xrange(2,n):
			tmp = max(dp0+nums[i],dp1)
			dp0 = dp1
			dp1 = tmp
		return max(dp0,dp1)
		
		