class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        if nums[pivot] <= target <= nums[n - 1]:
            l, r = pivot, n - 1
        else:
            l, r = 0, pivot - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1
        