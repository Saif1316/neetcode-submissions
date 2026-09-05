class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current_streak = 1
        longest = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                current_streak +=1
            else:
                 longest = max(longest, current_streak)
                 current_streak = 1
        longest = max(longest,current_streak)
        return longest

         
        