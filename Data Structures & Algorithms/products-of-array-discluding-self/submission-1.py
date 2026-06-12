class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # create a dummy array first with the same length as nums, we'll be using for storing left side products of a number
        output = [1 for n in nums]

        # calculate left side product of a number and store in output
        left = 1
        for n in range(len(nums)):
            output[n] = left
            left *= nums[n]
        
        # multiply the left product with the right one but go from back, so we can reuse the multiplied result, we dont have to calculate for each
        right = 1
        for n in range(len(nums)-1, -1, -1):
            output[n] *= right
            right *= nums[n]

        return output