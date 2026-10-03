class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store =  dict()
        for val in nums:
            store[val]=""

        maxCount = 0
        for val in nums:
            if val-1 in store.keys():
                continue
            else:
                count = 0
                while (True):
                    count += 1
                    if val+count in store.keys():
                        continue
                    else:
                        # no more consicutive elements
                        break
                
                maxCount = max(maxCount, count)
        
        return maxCount

        