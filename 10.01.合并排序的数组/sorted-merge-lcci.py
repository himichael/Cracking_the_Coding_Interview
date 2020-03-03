class Solution(object):
	def merge(self, A, m, B, n):
		"""
		:type A: List[int]
		:type m: int
		:type B: List[int]
		:type n: int
		:rtype: None Do not return anything, modify A in-place instead.
		"""
		if not A or not B:
			return A if A else B
			
		i = m-1
		j = n-1
		tail = m+n-1
		while i>=0 or j>=0:
			if i==-1:
				A[tail] = B[j]
				j -= 1
			elif j==-1:
				A[tail] = A[i]
				i -= 1
			elif A[i]>=B[j]:
				A[tail] = A[i]
				i -= 1
			else:
				A[tail] = B[j]
				j -= 1
			tail -= 1