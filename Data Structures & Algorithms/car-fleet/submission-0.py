class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse=True)
        stack = []
        for i in range(len(pair)):
            t = (target - pair[i][0]) / pair[i][1]
            if stack and t <= stack[-1]:
                continue
            stack.append(t)
        return len(stack)

        