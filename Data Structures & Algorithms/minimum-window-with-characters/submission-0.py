class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = countT.get(c,0) + 1

        need = len(countT)
        l = 0 
        matches = 0
        res = [-1,-1]
        resLen = float('inf')

        for r in range(len(s)):

            window[s[r]] = window.get(s[r],0) + 1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                matches += 1
            
            while matches == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    matches -= 1
                l += 1
        l , r = res

        return s[l:r+1] if resLen != float('inf') else ""        

            

                
            


