class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for key, freq in count.items():
            buckets[freq].append(key)

        
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            result.extend(buckets[i])

            if len(result) >= k:
                return result[:k]