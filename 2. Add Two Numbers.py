from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        l4 = l3
        carryOver = 0
        count = 0
        while True:
            if l1 == None:
                first = 0
            else:
                first = l1.val
                l1 = l1.next
            if l2 == None:
                seconde = 0 
            else:
                seconde = l2.val
                l2 = l2.next              
            l3.val = (first + seconde + carryOver) % 10
            carryOver = (first + seconde + carryOver) // 10
            if carryOver != 0 or l1 != None or l2 != None:
                l3.next = ListNode()
                
                l3 = l3.next
            else:
                break
        return l4
