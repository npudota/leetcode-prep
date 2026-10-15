class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        lead_fleet = 0.0
        res = 0

        for pos, s in sorted(zip(position,speed), reverse=True):

            t = (target-pos) / s
            if t <= lead_fleet:
                continue
            lead_fleet = t
            res += 1
        return res
                
                
            

        