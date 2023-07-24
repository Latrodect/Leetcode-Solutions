class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        for item in nums:
            if item != val:
                nums[counter] = item
                counter += 1
        return counter