class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        
        t_chars = {}
        window = {}
        for c in t:
            t_chars[c] = t_chars.get(c,0)+1
        
        have = 0
        need = len(t_chars)
        left = 0 
        resultLength = float('infinity')
        result = [-1,-1]
        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0)+1
            if s[right] in t_chars and window[s[right]] == t_chars[s[right]]:
                have+=1
            
            while have == need:
                if (right-left+1) < resultLength:
                    resultLength = right-left+1
                    result = [left,right]

                window[s[left]]-=1
                if s[left] in t_chars and window[s[left]] < t_chars[s[left]]:
                    have-=1
                left+=1
        left,right = result
        return s[left: right + 1] if resultLength != float('infinity') else ""

        
        