class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left = 1
        for n in range(len(nums)):
            output[n] = left
            left *= nums[n]

        right = 1
        for n in range(len(nums) - 1, -1, -1):
            output[n] *= right
            right *= nums[n]
        
        return output
        