class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        for num in freq:
            bucket[freq[num]].append(num)
        output = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                if (len(output) != k):
                    output.append(num)
        return output
