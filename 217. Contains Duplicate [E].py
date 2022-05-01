"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create hashmap to store values
        hashm = {}
        #iterate through values, if not in our hashmap, add it. otherwise return True (duplicate)
        for num in nums:
            if num in hashm:
                return True
            else:
                hashm[num] = 1
        
        return False

nums = [1,2,3,1]