﻿class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n<=0:
            return []
        res = []
        def dfs(left,right,tmp):
            if left==n and right==n:
                res.append(tmp)
                return
            if left<n:
                dfs(left+1,right,tmp+"(")
            if right<left and right<n:
                dfs(left,right+1,tmp+")")
        dfs(0,0,"")
        return res