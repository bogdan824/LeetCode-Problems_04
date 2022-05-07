"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #count the appearence of all the numbers
        a = nums.count(0)
        b = nums.count(1)
        c = nums.count(2)
        
        #append the appearence to the array 
        nums[0:a] = [0] * a
        nums[a:a+b] = [1] * b
        nums[a+b:] = [2] * c
        
        return nums

nums = [2,0,2,1,1,0]