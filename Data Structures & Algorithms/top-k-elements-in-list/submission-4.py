class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        minHeap = []
        for num in freq:
            heapq.heappush(minHeap, (-1 * freq[num], num))
        output = []
        for i in range(k):
            popped = heapq.heappop(minHeap)
            output.append(popped[1])
        return output
        