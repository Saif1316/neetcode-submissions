import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            left_subarray = math.prod(nums[0:i])
            right_subarray = math.prod(nums[i+1:len(nums)])
            result.append(left_subarray*right_subarray)
        return result
        