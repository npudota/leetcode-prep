class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = "".join(char for char in s if char.isalpha() or char.isdigit())
        letters = letters.lower()
        i = 0
        j = len(letters)-1
        while(i < j):
            if letters[i] != letters[j]:
                return False
            i += 1
            j -= 1
        return True
        

        