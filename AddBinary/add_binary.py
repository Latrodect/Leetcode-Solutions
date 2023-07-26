class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_len = len(a)-1
        b_len = len(b)-1
        carry = 0
        binary_sum = []

        while a_len >= 0 or b_len >= 0 or carry:
            total = carry
            if a_len >= 0:
                total += int(a[a_len])
                a_len -= 1
            if b_len >= 0:
                total += int(b[b_len])
                b_len -= 1
            binary_sum.append(str(total%2))
            carry = total / 2
        result = "".join(reversed(binary_sum))
        return result