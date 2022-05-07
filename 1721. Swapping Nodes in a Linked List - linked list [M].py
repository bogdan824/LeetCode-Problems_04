"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
"""

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #create array, store all the values
        result = []
        while head:
            result.append(head.val)
            head = head.next
        #swap the elements at k
        temp = result[k-1]
        result[k-1] = result[-k]
        result[-k] = temp
        #append everything to a new LL
        dummy = ListNode()
        tail = dummy
        
        for x,i in enumerate(result):
            tail.next = ListNode(i)
            tail = tail.next
        
        return dummy.next
head = [1,2,3,4,5]
k = 2