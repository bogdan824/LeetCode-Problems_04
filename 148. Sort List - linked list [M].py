"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #add all the nums from LL to an array
        result = []
        while head:
            result.append(head.val)
            head = head.next
        #sort the array
        result.sort()
        
        #create LL and add all the nums from the array
        dummy = ListNode()
        tail = dummy
        
        for x,i in enumerate(result):
            tail.next = ListNode(i)
            tail = tail.next
        
        return dummy.next
 head = [4,2,1,3]           