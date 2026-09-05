from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_common_elements = count.most_common(k)
        return [elements for elements,_ in most_common_elements]

        