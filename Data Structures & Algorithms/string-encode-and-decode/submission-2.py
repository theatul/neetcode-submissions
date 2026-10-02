class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            res = res+str(len(item))+"#"+item
        return res 


    def decode(self, s: str) -> List[str]:
        #print(s)
        res = []
        i = 0

        while i < len(s):
            # read length
            count = 0
            #print(i)
            while(s[i] != '#'):
                count = count*10 + int(s[i])
                i +=1
            maxindex= i + count
            i +=1
            
            # 5#fetch string
            temp = ""
            while (i <= maxindex):
                temp = temp+s[i]
                i +=1

            res.append(temp)
            #print (res)
            #i += 1
        
        return res







