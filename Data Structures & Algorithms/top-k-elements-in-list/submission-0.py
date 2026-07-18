class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Track the number of times an element occurs in nums
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        # Put elements into minHeap
        minHeap = []
        for num in hashmap:
            heapq.heappush(minHeap, (-1 * hashmap[num], num))
        output = []
        for i in range(k):
            item = heapq.heappop(minHeap) 
            output.append(item[1])
        return output