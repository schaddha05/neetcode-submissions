class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)



    def decode(self, s: str) -> List[str]:
        i = 0 
        decode = []
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            i = j + 1
            decode.append(s[i: i + length])
            i = i + length
        
        return decode 

