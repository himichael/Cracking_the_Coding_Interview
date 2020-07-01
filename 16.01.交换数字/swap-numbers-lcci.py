class Solution(object):
    def swapNumbers(self, numbers):
        """
        :type numbers: List[int]
        :rtype: List[int]
        """
        if not numbers:
            return []
        numbers[0],numbers[1] = numbers[1],numbers[0]
        return numbers
		
		
		
	# 使用加减法	
    def swapNumbers(self, numbers):
        numbers[0] = numbers[0]+numbers[1]
        numbers[1] = numbers[0]-numbers[1]
        numbers[0] = numbers[0]-numbers[1]
        return numbers
		
		
		
	# 使用异或运算
    def swapNumbers(self, numbers):
        numbers[0] ^= numbers[1]
        numbers[1] ^= numbers[0]
        numbers[0] ^= numbers[1]
        return numbers