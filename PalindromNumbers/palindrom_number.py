class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
       
        if x < 0:
            return False
        
        nums = [int(num) for num in str(x)]
        reversed_nums = list(reversed(nums))

        if nums == reversed_nums:
            return True
        return False

