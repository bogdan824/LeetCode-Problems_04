"""
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
"""

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
    	#create an array of length s
        answer = [a for a in range(len(s))]
    	#append each element 
        for i in range(len(s)):
            answer[indices[i]] = s[i]
        #return as string    
        return "".join(a for a in answer)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]            