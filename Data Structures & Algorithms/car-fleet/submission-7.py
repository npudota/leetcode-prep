class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = []
        for i in range(len(position)):
            pair.append([position[i],speed[i]])
        
        pair.sort(reverse=True)
        stack = []

        for p in pair:
            pos, s = p
            t = (target-pos) / s
            if stack and t <= stack[-1]:
                continue
            stack.append(t)
        return len(stack)
                
                
            

        