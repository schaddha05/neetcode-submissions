class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # sorted anagram -> [list of words]

        for s in strs:
            sort = ''.join(sorted(s))
            if sort not in anagrams:
                anagrams[sort] = []
            
            anagrams[sort].append(s)
        
        res = []
        for group in anagrams.values():
            res.append(group)
        return res

