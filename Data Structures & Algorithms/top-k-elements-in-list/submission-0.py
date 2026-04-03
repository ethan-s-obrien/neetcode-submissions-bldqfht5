from collections import Counter as counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_bucket = [[] for _ in range (len(nums) + 1)]
        counts = counter(nums)
        for n, c in counts.items():
            freq_bucket[c].append(n)
        res = []
        for i in range(len(freq_bucket) - 1, 0, -1):
            for n in freq_bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
