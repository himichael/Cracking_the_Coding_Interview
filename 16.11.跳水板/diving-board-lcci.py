class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        if k==0:
            return []
        if shorter==longer:
            return [k*shorter]
        dp = [0 for _ in xrange(k+1)]
        for i in xrange(k+1):
            dp[i] = shorter*(k-i) + longer*i
        return dp