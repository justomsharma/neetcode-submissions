class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque()  # stores indices, values decreasing
        result = []
        
        for i, num in enumerate(nums):
            # Remove indices out of window
            while dq and dq[0] <= i - k:
                dq.popleft()
            # Remove smaller elements from back
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)
            
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result