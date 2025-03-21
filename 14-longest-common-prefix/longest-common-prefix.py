class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        out = ''
        max_length = min(len(s) for s in strs) 
        letter = 0
        
        while letter < max_length:
            current_char = strs[0][letter]
            
            for string in strs:
                if string[letter] != current_char:  
                    return out
            out += current_char
            letter += 1
        
        return out



        