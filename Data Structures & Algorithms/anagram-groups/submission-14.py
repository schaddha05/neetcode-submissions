class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c)-ord('a')]+=1
            
            if tuple(count) in hashmap:
                hashmap[tuple(count)].append(word)
            else:
                hashmap[tuple(count)] = [word]
        
        return list(hashmap.values())
