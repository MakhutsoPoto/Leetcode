class Solution:
    import string 
    def isPalindrome(self, s: str) -> bool:
        m = s.lower()
        for n in m:
            if n in string.punctuation or n ==" ":
                m = m.replace(n,"")
        if m== m[::-1]:
            return True
        return False
        