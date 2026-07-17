class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            # Create a "code" for each string based on its letters.
            code = [0] * 26
            for c in s:
                code[ord(c) - ord('a')] += 1
            # Map the string to its corresponding code in the hashmap
            hashmap[tuple(code)].append(s)
        output = []
        for code in hashmap:
            output.append(hashmap[code])
        return output
        

