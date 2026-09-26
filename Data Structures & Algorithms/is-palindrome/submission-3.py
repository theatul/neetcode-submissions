class Solution:
    def isPalindrome(self, s: str) -> bool:

        forward = 0
        back = len(s) - 1

        if forward == back:
            return True
        
        while (forward < back) and forward < len(s) and back >= 0:
            while forward < len(s) and not s[forward].isalnum():
                forward += 1
            while back >= 0 and  not s[back].isalnum():
                back -= 1
            
            if (forward >= back):
                return True
            
            if (s[forward].upper() != s[back].upper()):
                print(s[forward])
                print(s[back])
                return False
            
            forward += 1
            back -= 1
            
        return True

            
        