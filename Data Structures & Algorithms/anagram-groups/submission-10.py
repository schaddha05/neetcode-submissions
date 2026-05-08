class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in range(len(strs)):
            sort_str = tuple((sorted(strs[i])))
            if sort_str in hashmap:
                hashmap[sort_str].append(strs[i])
            else:
                hashmap[sort_str] = [strs[i]]

        return hashmap.values()
    