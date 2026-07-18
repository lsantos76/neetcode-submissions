class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(list)
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        for num in hashmap:
            count[hashmap[num]].append(num)
        output = []
        for i in range(len(nums), -1, -1):
            if count[i] != []:
                for n in count[i]:
                    if len(output) == k:
                        break
                    output.append(n)
        return output
