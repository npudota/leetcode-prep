class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse=True)
        fleet = 0
        longest = 0
        for p, s in pair:
            t = (target - p) / s
            if t <= longest:
                continue
            longest = t
            fleet += 1
        return fleet

        