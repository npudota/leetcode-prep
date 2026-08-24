class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #pair(index, height)
        maxArea = 0

        for i , height in enumerate(heights):
            startIndex = i
            while stack and height < stack[-1][1]:
                j, h = stack.pop()
                w = i - j
                maxArea = max(maxArea, h * w)
                startIndex = j
            stack.append((startIndex , height))
        for i , h in stack:
            w = len(heights) - i
            maxArea = max(maxArea, h * w)
        return maxArea

        