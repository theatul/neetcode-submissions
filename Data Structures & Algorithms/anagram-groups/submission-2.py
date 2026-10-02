class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for item in strs:
            array = [0]*26
            for c in item:
                array[ord(c)- ord('a')] += 1
            res[tuple(array)].append(item)
        return list(res.values())