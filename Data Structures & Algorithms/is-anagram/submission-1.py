class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        array = [0]*26
        for c in s:
            array[ord(c)-ord('a')] += 1
        
        print(array)
        for c in t:
            array[ord(c)-ord('a')] -= 1

        print(array)
        for i in range(26):
            if array[i] != 0:
                return False
        
        return True
        