class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i,value in enumerate(nums):
            difference = target - value
            if difference in nums_dict:
                return [nums_dict[difference],i]
            nums_dict[value]=i
 
        