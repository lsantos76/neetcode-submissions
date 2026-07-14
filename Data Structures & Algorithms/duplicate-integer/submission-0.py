class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Go through array, putting each element into set
        hashset = set()
        for n in nums:
            # If we already have n in our set, return True.
            if n in hashset:
                return True
            hashset.add(n)
        # We have gone through the whole array with no duplicate.
        return False