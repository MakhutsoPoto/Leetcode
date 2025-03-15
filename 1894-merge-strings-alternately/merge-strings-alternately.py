class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        zipped = zip(word1,word2)
        merge = ""
        for letter1,letter2 in zipped:
                merge +=letter1 + letter2
        merge+=word1[len(word2):]
        merge +=word2[len(word1):]


        result = ''.join(merge)

        return result
        