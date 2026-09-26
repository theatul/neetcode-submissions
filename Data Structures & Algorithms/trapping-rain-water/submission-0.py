class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_list = [0]*n
        right_list = [0]*n

        # build left
        left_list[0] = height[0]
        for i in range (1,n):
            left_list[i] = max(left_list[i-1], height[i])
        
        # Build right
        right_list[n-1] = height[n-1]
        for i in range (n-2, -1, -1):
            right_list[i] = max(right_list[i+1],  height[i])
        
        # Calculate total water
        total_water = 0
        for i in range (n):
            temp = min(left_list[i], right_list[i]) - height[i]
            if temp > 0:
                total_water = total_water + temp
        
        return total_water





        