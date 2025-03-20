class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in parentheses:
                stack.append(char)
            else:
                
                if not stack or parentheses[stack.pop()] != char:
                    return False

        
        return not stack
