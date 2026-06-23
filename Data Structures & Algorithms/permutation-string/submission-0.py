class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key_s1 = tuple(sorted(s1))

        right = len(s1)
        for left in range(len(s2)):
            key_s2 = tuple(sorted(s2[left:right]))
            if key_s1 == key_s2:
                return True
            right += 1
        
        return False




