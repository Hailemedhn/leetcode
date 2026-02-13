from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverses Nodes in k-group by moving three (left, center and right) pointers left one step at a time and connecting the center to the left except when the center is at the k-th position. 
        """
        beg1,left = head,head
        center = left.next
        right = center.next if center is not None else None
        step = 0
        beg2 = None
        length,i = 0,2

        #find out the length of the list
        curr = head
        while curr is not None:
            curr = curr.next
            length += 1
        limit = length - length % k
        if k >= 2:
            while i <= limit:
                #Move the three pointers left one step at a time and connect the center to the left except when the center is at the beginning of a new group.
                while (i - 1) % k != 0:
                    center.next = left
                    left = center
                    center = right
                    right = right.next if right is not None else None
                    i += 1
                step += 1
                #if it is the first pass then the left is in the head of the newly arranged list
                if step == 1:
                    head = left 
                    beg2 = center
                #the begining of the first k-goup would be connected to the left of the newly arraged k-group
                else:
                    beg1.next = left
                    beg1 = beg2
                    beg2 = center
                #if right is not None then move the three pointers left on step with out connecting the center to the left.
                if right is not None:
                    i += 1
                    left = center
                    center = right
                    right = right.next
                #if right is None we are at the end of the left movement and the we connect the last beg1 to the center and get out of the loop by returning head. This means the length of the list is a multiple of k
                else:
                    beg1.next = center
                    return head
            #if the length of the list is not a multiple of k we connect beg1 to the left pointer which now points to the first of the remaining nodes.
            beg1.next = left
        return head
