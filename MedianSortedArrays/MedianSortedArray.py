class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        concat_arr = nums1+nums2
        concat_arr.sort()
        length = len(concat_arr)
        print(length)
        if length % 2 == 0:
            up_center = length / 2
            down_center  = up_center - 1
            print(float(concat_arr[up_center]))
            print(float(concat_arr[down_center]))
            total = float(concat_arr[up_center]) + float(concat_arr[down_center]) 
            median = total / 2
            return median
            
        else:
            center = length / 2
            median = float(concat_arr[center])
            return median
