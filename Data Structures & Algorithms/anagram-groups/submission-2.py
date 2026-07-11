class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = {}

        for c in strs:
            key = tuple(sorted(c))
            group_anagram[key] = group_anagram.get(key, []) + [c]
        
        return list(group_anagram.values())
            

