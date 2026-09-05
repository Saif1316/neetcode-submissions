from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        count = Counter(nums)
        for key in count:
            if count[key] > 1:
                return True
        return False
         