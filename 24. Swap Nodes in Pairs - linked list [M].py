"""
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)
"""

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0)
        prev.next = head
        
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            c = prev.next.next.next
            
            prev.next = b
            prev.next.next = a
            prev.next.next.next = c
            
            prev = prev.next.next
        
        return dummy.next
head = [1,2,3,4]

