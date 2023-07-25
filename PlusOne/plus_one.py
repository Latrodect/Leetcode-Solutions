class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        concat = "".join(str(num) for num in digits)
        num = str(int(concat) + 1)
        n_digits = [int(n) for n in num]
        
        return n_digits