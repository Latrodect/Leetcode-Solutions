class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }

        total = 0
        prev_value = 0
        for num in s[::-1]:
            val = roman_values[num]
            if val < prev_value:
                total -= val
            else:
                total += val
            prev_value = val

        return total