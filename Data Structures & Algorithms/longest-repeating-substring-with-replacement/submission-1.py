class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        mp = {}
        l = 0
        res = 0
        
        max_value = 0
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r],0) + 1
            max_value = max(mp[s[r]], max_value) 
            while (r - l + 1) - max_value > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        
        return res

        