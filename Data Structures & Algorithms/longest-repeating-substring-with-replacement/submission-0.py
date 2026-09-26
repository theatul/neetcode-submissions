class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        max_len, res = 0, 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] +=1
            
            max_len = max(max_len, count[s[r]])

            while (r-l+1) - max_len > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res


