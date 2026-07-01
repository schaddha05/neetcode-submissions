class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''

        for string in strs:
            s += str(len(string)) + '#' + string
    
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            content = s[j + 1: j + length + 1]
            res.append(content)
            i = j + length + 1
        
        return res


        
        
        
        return res
