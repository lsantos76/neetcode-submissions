class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check the length of both strings
        if len(s) != len(t):
            return False
        # Create hashmaps for both strings
        hashmap1, hashmap2 = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            hashmap1[s[i]] += 1
            hashmap2[t[i]] += 1
        # Compare hashmaps
        for c in hashmap1:
            if hashmap1[c] != hashmap2[c]:
                return False
        return True