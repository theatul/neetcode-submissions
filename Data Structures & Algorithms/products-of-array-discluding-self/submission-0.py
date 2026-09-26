class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #forward_product = [0 for i in range(len(nums))]
        forward_product = [0]*len(nums)
        backward_product = [0 for i in range(len(nums))]

        nums_len = len(nums)
        
        forward_product[0] = nums[0]
        for i in range(1, nums_len):
            forward_product[i] =  forward_product[i-1]*nums[i]

        backward_product[nums_len -1] = nums[nums_len -1]
        for i in range(nums_len-2, -1, -1):
            backward_product[i] = backward_product[i+1] * nums[i]

        
        # out put
        out = [0 for i in range (len(nums))]
        out[0] = backward_product[1]
        out[nums_len-1] = forward_product[nums_len-2]
        for i in range(1, nums_len-1):
            out[i] = forward_product[i-1] * backward_product[i+1]
        
        return out


    

