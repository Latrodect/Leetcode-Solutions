class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        point_one = m - 1
        point_two = n - 1
        merge_point = m + n - 1

        while point_one >= 0 and point_two >= 0:
            if nums1[point_one] >= nums2[point_two]:
                nums1[merge_point] = nums1[point_one]
                point_one -= 1
            else:
                nums1[merge_point] = nums2[point_two]
                point_two -= 1

            merge_point -= 1

        while point_two >= 0:
            nums1[merge_point] = nums2[point_two]
            merge_point -= 1
            point_two -= 1
            
        return nums1

