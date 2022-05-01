"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #store the powers of 2
        keep = [2**i for i in range(100)]
        #check if n in keep
        if n in keep:
            return True
        return False

n = 1
#n=16
#n=3