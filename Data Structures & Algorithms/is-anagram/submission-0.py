class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map = {}
        for i in range(len(s)):
            s_ch = s[i]
            if s_ch in map:
                map[s_ch] = map[s_ch]+1
            else:
                map[s_ch] = 1

            t_ch = t[i]
            if t_ch in map:
                map[t_ch] = map[t_ch] - 1
            else:
                map[t_ch] = -1
        
        for key, val in map.items():
            if val != 0:
                return False
        
        return True
        