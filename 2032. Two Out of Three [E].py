"""
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
"""

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        hashm = {}
        #remove duplicates
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = list(set(nums3))
        #append everything to hashmap
        for a in nums1:
            if a in hashm:
                hashm[a]+=1
            else:
                hashm[a]=1
        
        for a in nums2:
            if a in hashm:
                hashm[a]+=1
            else:
                hashm[a]=1
                
        for a in nums3:
            if a in hashm:
                hashm[a]+=1
            else:
                hashm[a]=1
        result = []
        
        for key, value in hashm.items():
            if value > 1:
                result.append(key)
        
        return result
    
#or return set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3)