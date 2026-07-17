class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            sortedS = sorted(s)
            hashmap[tuple(sortedS)].append(s)
        return list(hashmap.values())
        
    