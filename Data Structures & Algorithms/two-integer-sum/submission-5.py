class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hashmap = {}

        for i, n in enumerate(nums):

            complement = target - n
            if complement in Hashmap:
                return [Hashmap[complement], i]
            Hashmap[n] = i
        return 


        