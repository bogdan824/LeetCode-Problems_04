"""
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.
"""

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        #any sum of the power of three has to be in a form of 3^n or 3^(n+1)=3^n + 3^0
        #So the if condition makes sure of that and we keep dividing n 3 until it eventually becomes 1 and returns True
        while(n>=1):
            if n%3==2: return False
            n=n//3
        return True