class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        res = 0

        leftMax[0] = height[0]
        for i in range(1, len(height)):
            leftMax[i] = max(height[i],leftMax[i-1])

        rightMax[len(height)-1] = height[len(height)-1]
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1])
        

        for i,h in enumerate(height):
            res += min(rightMax[i], leftMax[i]) - h
        return res

        


        