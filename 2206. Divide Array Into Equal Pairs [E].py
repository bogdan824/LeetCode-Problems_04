"""
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
"""

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        #hashmap to store all the values and their freq
        hashm = {}
        for num in nums:
            if num in hashm:
                hashm[num]+=1
            else:
                hashm[num]=1
        
        #for each value, if is not div by 2, it means t does not satisfy the condition
        for key, value in hashm.items():
            if value % 2 != 0 :
                return False
        return True

nums = [3,2,3,2,2,2]