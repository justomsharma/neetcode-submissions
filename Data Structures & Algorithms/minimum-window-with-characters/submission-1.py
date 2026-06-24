class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        need = {}
        missing = len(t)
        left, best_left = 0, 0
        best_length = float('inf')

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        for right, ch in enumerate(s):
            if need.get(ch, 0) > 0:
                missing -= 1
            need[ch] = need.get(ch, 0) - 1

            while missing == 0:
                if right - left + 1 < best_length:
                    best_length, best_left = right - left + 1, left
                
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        
        return "" if best_length == float('inf') else s[best_left:best_left + best_length]