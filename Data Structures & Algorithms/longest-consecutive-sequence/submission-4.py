class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0

        num = set(nums)

        for n in num:
            if n + 1 in num:
                continue
            i = n
            count = 0
            while i in num:
                count += 1
                i -= 1
            res = max(count,res)
        return res
        