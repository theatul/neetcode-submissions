class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        buckets = [[] for i in range(len(nums)+1)]

        for val in nums:
            if val in count_map.keys():
                count_map[val] =  count_map[val] +1
            else:
                count_map[val] = 1
        
        # Bucket sort
        for num, count in count_map.items():
            buckets[count].append(num)
        
        temp = k
        out = []
        for i in range (len(nums), 0, -1):
            if buckets[i]:
                j = 0
                while temp != 0 and j < len(buckets[i]) :
                    print (buckets)
                    print (i,j)
                    out.append(buckets[i][j])
                    temp = temp -1
                    j = j +1

        return out




        