class Solution(object):
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: None Do not return anything, modify matrix in-place instead.
		"""			
		if not matrix:
			return 
		n = len(matrix)
		for i in xrange(n/2):
			matrix[i],matrix[n-i-1] = matrix[n-i-1],matrix[i]
		for i in xrange(n):
			for j in xrange(i):
				matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
				
				
				
	def rotate(self, matrix):
		matrix[:] = zip(*reversed(matrix))