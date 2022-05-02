"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        #as long the number has more than one digit
        while num > 9:
            suma=0
            #we add all the digits of the num
            while num > 0:
                suma += num%10
                num//=10
            num=suma
        #if sum of all digits is one digit, return it
        return num  
    
num = 38