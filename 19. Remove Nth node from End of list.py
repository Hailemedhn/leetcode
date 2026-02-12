from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Delete `node` at n-th place from end.

        Policy:
        - n >= length  -> delete the first item
        - n <= 0 -> do nothing

        Returns the (possibly new) head.
        """
        length = 1
        node = head
        while node.next is not None:
            node = node.next
            length += 1
        n = length - n
        # Deleting from an empty LinkedList just returns the empty LinkedList   
        if head is None:
            return head
        # For negative pos values or when pos == 0 delets the head
        if n <= 0:
            curr = head.next
            head.next = None
            return curr
        
        # prepate to walk the list with refrence to the current and previous nodes
        prev = head
        curr = head.next
        step = n - 1

        # The case where the linkedlist is just one node long
        if curr is None:
            return head
        #wallk the list for a list longer than 1 node
        while step > 0 and curr.next is not None :
            prev = curr
            curr = curr.next
            step -= 1
        #for deleting from the middle or the tail of the list
        if step == 0:
            prev.next = curr.next
        
        return head