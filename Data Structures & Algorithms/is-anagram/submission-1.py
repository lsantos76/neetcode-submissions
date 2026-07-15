class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings then compare
        return sorted(s) == sorted(t)