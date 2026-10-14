class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        water = 0
        smallerEdge = 0
        leftedges = [0] * len(height)
        rightedges = [0] * len(height)

        largest = 0
        for i, n in enumerate(height):
            largest = max(n, largest)
            leftedges[i] = largest
        largest = 0
        for i in range(len(height) - 1, -1,-1):
            largest = max(height[i], largest)
            rightedges[i] = largest
        
        for i,n in enumerate(height):
            val = min(leftedges[i],rightedges[i]) - n
            if val > 0:
                water += val

        return water
        





        