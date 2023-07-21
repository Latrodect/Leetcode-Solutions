import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_of_index = []
        for num in nums: 
  
            second_int = target - num
            second_int_count = nums.count(second_int)
            print(second_int_count)
            if(second_int in nums and second_int_count==1 and num != second_int):
                list_of_index.append(nums.index(num))
                list_of_index.append(nums.index(second_int))
                break
            elif(second_int in nums and second_int_count==1 and num == second_int):
                continue
            elif(second_int in nums and second_int_count>1):
                list_of_index = self.find_indices(nums, second_int)
                print(list_of_index)
                break
            
        return list_of_index

    def find_indices(self, list_to_check, item_to_find):
        indices = []
        for idx, value in enumerate(list_to_check):
            if value == item_to_find:
                indices.append(idx)
        return indices