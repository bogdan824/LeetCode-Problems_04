"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #dumb solution
        #create two arrays and store the values, ort them and then compare
        s1 = []
        t1 = []
        for ch in s:
            s1.append(ch)
        for ch in t:
            t1.append(ch)
        s1.sort()
        t1.sort()
        
        return s1 == t1
 s = "anagram"
 t = "nagaram"           