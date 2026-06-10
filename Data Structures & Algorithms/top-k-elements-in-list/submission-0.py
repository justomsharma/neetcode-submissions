class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for i in nums:
            seen[i] = seen.get(i, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for key, freq in seen.items():
            buckets[freq].append(key)
        
        result = []
        for i in range(len(buckets)-1, 0, -1):
            result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]