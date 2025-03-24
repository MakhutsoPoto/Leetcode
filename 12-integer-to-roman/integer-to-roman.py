class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 
            'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 
            'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I':1}#roman equivalent to modern numbers
        roman_numerals = "" #initialize my variable into an empty string 
        for number in reversed(sorted(numerals.keys(), key =numerals.get)):#sort in descending order reverse list and sort
            while num >= numerals[number]:#number if greater or equal to the given number value,add
                roman_numerals += number #true?add numeral 
                num -= numerals[number] #reduces given by that number 
        return roman_numerals
                
