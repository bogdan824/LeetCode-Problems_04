"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #create a hashmap and store all values
        
        hashm = {}
        n = len(nums)
        for num in nums:
            if num in hashm:
                hashm[num]+=1
            else:
                hashm[num]=1
        #iterate through the elements and append to an array result
        result = []
        
        for key,value in hashm.items():
            if value > n/2:
                return key

nums = [3,2,3]