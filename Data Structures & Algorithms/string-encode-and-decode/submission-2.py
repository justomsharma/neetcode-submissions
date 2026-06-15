class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # encode the string in this way : length of the string, # (to let know that string starts from here), string itself
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        
        return encoded


    def decode(self, s: str) -> List[str]:
        
        # start decoding : use two pointers : i - pointer for the string, j - pointer for the length and identify for start and end point

        result = []
        i = 0
        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            end = start + length
            result.append(s[start:end])

            i = end
        
        return result
        