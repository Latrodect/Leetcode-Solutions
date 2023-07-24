class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        for index, item in enumerate(nums):
            if index == 0 :
                continue
            if nums[index] != nums[index - 1]:
                nums[counter] = item
                counter += 1
        return counter


            


            
