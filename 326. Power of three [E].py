"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #store the powers of 2
        keep = [3**i for i in range(100)]
        #check if n in keep
        if n in keep:
            return True
        return False
