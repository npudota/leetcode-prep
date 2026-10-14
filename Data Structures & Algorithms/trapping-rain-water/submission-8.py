class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        water = 0

        maxL = 0
        maxR = 0
        while l < r:
            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)
            if height[l] < height[r]:
                water += max(min(maxL,maxR) - height[l],0)
                l += 1
            else:
                water += max(min(maxL,maxR) - height[r],0)
                r -= 1

        return water

        





        