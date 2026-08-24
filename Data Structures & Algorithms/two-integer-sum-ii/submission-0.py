class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while(i < j):
            s = numbers[i] + numbers[j]
            if target == s:
                break
            elif target > s:
                i += 1
            elif target < s:
                j -= 1
        return ([i+1, j+1])
        