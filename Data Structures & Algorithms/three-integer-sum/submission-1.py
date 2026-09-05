class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        target = 0
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            if i > 0 and nums[i]==nums[i-1]:
                continue
            while j < k:
                if nums[i]+nums[j]+nums[k]>target:
                    k-=1
                elif nums[i]+nums[j]+nums[k]<target:
                    j+=1
                elif nums[i]+nums[j]+nums[k]==target:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j < k:
                        j += 1
        return result
        