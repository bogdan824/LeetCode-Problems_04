"""
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
"""

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        #helper function to check if palindrome
        def checkPal(num):
            start = 0
            end = len(num)-1
            while start < end:
                if num[start] == num[end]:
                    start += 1
                    end -= 1
                else:
                    return 0
            # 1 means palindrome - 0 means no plaindrome
            return 1
            
    
        for num in words:
            x = checkPal(num)
            #if palindrome, return
            if x == 1:
                return num
        return ""
words = ["abc","car","ada","racecar","cool"]            