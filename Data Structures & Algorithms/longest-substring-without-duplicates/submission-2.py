class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        if n == 1:
            return 1

        cache_map = {}
        i, j = 0, 0
        max_len = 0
        while (i < n) & (j < n):
            while s[j] in cache_map:
                del cache_map[s[i]]
                i += 1

            cache_map[s[j]] = j
            max_len = max(max_len, j-i +1)
            j = j+1
        
        return max_len


        