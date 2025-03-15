class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        m =s.strip().split()
        index = len(m)-1 
        return len(m[index])