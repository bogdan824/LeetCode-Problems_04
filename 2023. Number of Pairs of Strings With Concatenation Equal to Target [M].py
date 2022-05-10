"""
Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.
"""

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        result = 0
        #check every combination of numbers
        for i in range(len(nums)):
            for j in range(len(nums)):
                #if matches the requirement, we increase the result by 1
                if i != j and nums[i]+nums[j] == target:
                    result +=1 
        return result
 nums = ["777","7","77","77"]
 target = "7777"
                    