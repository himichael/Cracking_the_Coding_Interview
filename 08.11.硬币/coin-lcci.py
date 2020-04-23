class Solution(object):
	def waysToChange(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		coins = (1,5,10,25)
		dp = [0]*(n+1)
		dp[0] = 1
		for c in coins:
			for i in xrange(c,n+1):
				dp[i] += dp[i-c]+1
		return dp[-1]%1000000007