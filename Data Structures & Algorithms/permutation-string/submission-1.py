class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        
        s1f, s2f = [0]*26, [0]*26
        for i in range(len(s1)):
            s1f[ord(s1[i])- ord('a')] += 1
            s2f[ord(s2[i])- ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1f[i] == s2f[i]:
                matches += 1

        if matches == 26:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            # Remove left from the window
            index = ord(s2[l]) - ord('a')
            s2f[index] -= 1
            if s1f[index] == s2f[index]:
                matches += 1
            elif s1f[index] == s2f[index]+1:
                matches -= 1
            l += 1

            # Addd right to the window
            index = ord(s2[r]) - ord('a')
            s2f[index] += 1
            if s1f[index] == s2f[index]:
                matches += 1
            elif s1f[index] == s2f[index] - 1:
                matches -=1
            
            if matches == 26:
                return True
        
        return False

            

        