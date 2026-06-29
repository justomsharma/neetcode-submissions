class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # use two pointer approach
        left = 0
        right = len(numbers) - 1

        # iterate through each element till left is smaller than right
        while left < right:

            # calculate the sum of values of left pointer and right pointer
            current_sum = numbers[left] + numbers[right]

            # check if the sum is equal : then return the pointers + 1 for both pointers
            if current_sum == target:
                return [left + 1, right + 1]

            # if sum is smaller than target : we need bigger sum : move left pointer
            elif current_sum < target:
                left += 1
            
            # else we need smaller sum : move right pointer
            else:
                right -= 1
                