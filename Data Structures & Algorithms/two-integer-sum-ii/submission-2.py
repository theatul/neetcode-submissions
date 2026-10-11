class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) <= 1:
            return []
        
        left = 0
        right = len(numbers) -1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        
        return []
             
        