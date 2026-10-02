class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        fp = [1]*l
        bp = [1]*l
        
        fp[0] = 1
        for i in range (1, len(nums)):
            fp[i] = fp[i-1] * nums[i-1]
        
        #print(fp)

        bp[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            bp[i] = bp[i+1]*nums[i+1]

        #print(bp)

        prod = [1]*l
        for i in range(len(nums)):
            prod[i] = fp[i] * bp[i]

        return prod  
        