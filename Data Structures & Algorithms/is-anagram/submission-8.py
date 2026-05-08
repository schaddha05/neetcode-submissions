class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for c in s:
            letters[c] = letters.get(c, 0) + 1 
        
        for c in t:
            if c in letters:
                letters[c] -= 1 
                if letters[c] == 0:
                    del letters[c] 
            else:
                letters[c] = 1
        
        if len(letters) == 0:
            return True
        else:
            return False 