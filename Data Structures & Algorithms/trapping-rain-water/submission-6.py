class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = height[0]
        maxRight = height[len(height) - 1]
        trap = 0

        l, r = 0 , len(height) - 1

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                trap += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                trap += maxRight - height[r]
        return trap


        


        