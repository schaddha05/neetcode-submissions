class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # tuple of char frequencies -> [list of words]

        for s in strs:
            frequency = [0] * 26
            for c in s:
                frequency[ord(c) - ord('a')] += 1
            
            if tuple(frequency) not in anagrams:
                anagrams[tuple(frequency)] = []
            
            anagrams[tuple(frequency)].append(s)     
        
        return list(anagrams.values())

