class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for letter in t:
            if t.count(letter) > s.count(letter):
                return letter
        