class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        current = x
        for i in range(1, 50000):
            pw_number = i*i
            if pw_number > x:
                break
            else:
                current = i
        return current
        
