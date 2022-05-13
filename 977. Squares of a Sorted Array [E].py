"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        
        for num in nums:
            result.append(num*num)
        
        result.sort()
        return(result)
        
nums = [-4,-1,0,3,10]