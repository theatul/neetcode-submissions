class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            arr = [0]*26
            for c in str:
                arr[ord(c)-ord('a')] += 1
            res[tuple(arr)].append(str)
        
        return list(res.values())

        