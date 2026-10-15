class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = []
        for i in range(len(position)):
            pair.append([position[i],speed[i]])
        
        pair.sort(reverse=True)
        lead_fleet = 0.0
        res = 0

        for p in pair:
            pos, s = p
            t = (target-pos) / s
            if t <= lead_fleet:
                continue
            lead_fleet = t
            res += 1
        return res
                
                
            

        