"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #create empty array to store nums
        result = []
        #index to insert to nums at
        evPos = 0
        #loop through array
        for num in nums:
            #if even insert at index
            if num%2==0:
                result.insert(evPos,num)
                evPos+=1
            #if odd append at the end
            else:
                result.append(num)
        return result

nums = [3,1,2,4]