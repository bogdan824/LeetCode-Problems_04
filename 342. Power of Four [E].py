"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #store the powers of 2
        keep = [4**i for i in range(100)]
        #check if n in keep
        if n in keep:
            return True
        return False