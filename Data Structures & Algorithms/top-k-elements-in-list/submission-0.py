class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        return [num for num,_ in freq.most_common(k)]