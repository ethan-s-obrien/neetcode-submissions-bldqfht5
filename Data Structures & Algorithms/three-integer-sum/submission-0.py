class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        res = []
        for i, a in enumerate(s_nums):
            if a > 0: break
            if i > 0 and a == s_nums[i-1]: continue
            b, c = i + 1, len(s_nums) - 1
            while b < c:
                three_sum = a + s_nums[b] + s_nums[c]
                if three_sum > 0:
                    c -= 1
                elif three_sum < 0:
                    b += 1
                else:
                    res.append([a, s_nums[b], s_nums[c]])
                    b += 1
                    while s_nums[b] == s_nums[b-1] and b < c:
                        b += 1
                
        return res
            
