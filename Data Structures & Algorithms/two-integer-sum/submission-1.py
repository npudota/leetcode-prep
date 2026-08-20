class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in complement:
                return [complement.get(diff), n]
            complement[nums[n]] = n
        
        