class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_str = min(strs)
        max_str = max(strs)

        for i in range(len(min_str)):
            if min_str[i] != max_str[i]:
                return min_str[:i]

        return min_str


        
            