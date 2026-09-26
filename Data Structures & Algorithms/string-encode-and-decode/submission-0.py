class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            length = len(string)
            out = out + str(length) +"#"+string
        return out


    def decode(self, s: str) -> List[str]:
        out = []

        i = 0
        while i < len(s):
            # get length
            count_str = ""
            while i < len(s) and s[i] != "#":
                count_str = count_str + s[i]
                i += 1
            
            # skip the #
            i += 1

            j = 0
            temp = ""
            while i < len(s) and j < int(count_str):
                temp = temp + s[i]
                i = i+1
                j = j+1
            
            out.append(temp)
        
        return out


            


