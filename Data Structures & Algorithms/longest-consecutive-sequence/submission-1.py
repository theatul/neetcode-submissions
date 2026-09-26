class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return  len(nums)
        
        store = set(nums)
        max_val = 0
        for val in store:
            if (val-1) in store:
                continue
            length = 1
            while val + length in store:
                length = length+1
            
            max_val = max(max_val, length)
        
        return max_val



        