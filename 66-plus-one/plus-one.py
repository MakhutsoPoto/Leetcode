class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for digit in digits:
            string += str(digit)
        newvalue = int(string) + 1
        final = []
        for number in str(newvalue) :
            final.append(int(number))
        return final
        