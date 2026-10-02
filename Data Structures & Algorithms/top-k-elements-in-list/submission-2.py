class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0 or len(nums) == 0:
         return []

        arr = [[] for _ in range(len(nums)+1) ]

        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1
        
        for num, count in countMap.items():
            arr[count].append(num)
        
        res = []
        for i in range(len(arr)-1, 0, -1):
            for item in arr[i]:
                res.append(item)
                if len(res) == k:
                    return res
           
        return res


