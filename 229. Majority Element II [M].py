"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
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
            if value > n/3:
                result.append(key)
        
        return result
        
nums = [3,2,3]    