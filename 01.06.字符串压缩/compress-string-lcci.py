class Solution(object):
	def compressString(self, S):
		"""
		:type S: str
		:rtype: str
		"""
		if not S:
			return S
		i = 0
		j = 0
		n = len(S)
		res = ""
		while i<n:
			while j<n and S[i]==S[j]:
				j += 1
			res += S[i] + str(j-i)
			i = j
		if len(res)>=n:
			return S
		return res