class Solution:
    def isPalindrome(self, s: str) -> bool:

        # use two pointers
        left = 0
        right = len(s) - 1

        # till left is smaller than right iterate through each character
        while left < right:

            # skip the non alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1
            
            # compare the values at both the pointers
            if s[left].lower() != s[right].lower():
                return False
            
            # move pointers inwards
            left += 1
            right -= 1
        
        return True
