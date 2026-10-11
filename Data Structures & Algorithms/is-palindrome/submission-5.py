class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        #covert to lower
        s = s.lower()
        
        def isalphanum(c):
            if ((ord(c) >= ord('a') and ord(c) <= ord('z')) or
            (ord(c) >= ord('A') and ord(c) <= ord('Z')) or
            (ord(c) >= ord('0') and ord(c) <= ord('9'))):
                return True
            
            return False
        
        
        i = 0
        j = len(s) -1

        while i < j:
            if not isalphanum(s[i]):
                i += 1
                continue
            if not isalphanum(s[j]):
                j -= 1
                continue
            
            if s[i] != s[j]:
                #print (s[i])
                #print (s[j])
                return False
            else:
                i += 1
                j -= 1
        
        return True
            
            

        