class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        sCount = [0] * 26
        tCount = [0] * 26
        for n in range(len(s)):
            sCount[ord(s[n])-ord('a')] +=1
            tCount[ord(t[n])-ord('a')] +=1
        if(sCount == tCount):
            return True
        return False

        


        