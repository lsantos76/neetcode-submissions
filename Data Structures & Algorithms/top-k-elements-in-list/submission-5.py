class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        array = []
        for num in freq:
            array.append([freq[num], num])
        array = sorted(array)
        output = []
        for i in range(len(array) - 1, -1, -1):
            output.append(array[i][1])
            if len(output) == k:
                return output

