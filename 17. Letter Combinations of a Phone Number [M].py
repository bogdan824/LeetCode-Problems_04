"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #create a mapping of the numbers with the corresponding values
        phone_map = { "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs","8" : "tuv", "9" : "wxyz",}
        
        #edge case - check if the string is empty
        if digits == "":
            return []
        
        #start by initialising a list that is just a posibility for the first chars in the input
        numbers = list(phone_map[digits[0]])
        
        #loop through any aditional digits
        for digit in digits[1:]:
            numbers = [old+new for old in numbers for new in list(phone_map[digit])]
            
        return numbers

 digits = "23"