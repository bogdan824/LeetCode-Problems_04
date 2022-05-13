"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #lower the string
        s = s.lower()
        #take 2 pointers
        start = 0 
        end = len(s)-1
        #check if letter
        while start < end:
            while start < end and not s[start].isalnum():
                start+=1
            while start < end and not s[end].isalnum():
                end-=1
            if s[start] != s[end]:
                return False
            start +=1 
            end -= 1
        return True
s = "A man, a plan, a canal: Panama"
#s = "race a car"                