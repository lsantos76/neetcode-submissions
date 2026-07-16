class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, n in enumerate(nums):
            A.append([n, i])
        A = sorted(A)
        low, high = 0, len(A) - 1
        while low < high:
            if A[low][0] + A[high][0] == target:
                return [min(A[low][1], A[high][1]), max(A[low][1], A[high][1])]
            elif A[low][0] + A[high][0] < target:
                low += 1
            else:
                high -= 1