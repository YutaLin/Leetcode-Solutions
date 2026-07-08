# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        mod = 0
        e = 0
        head_1 = l1
        head_2 = l2
        tail = l1
        while head_1 and head_2:
            s = head_1.val + head_2.val + e
            mod = s % 10
            e = s // 10
            
            head_1.val = mod
            tail = head_1
            head_1 = head_1.next
            head_2 = head_2.next

        if head_2:
            tail.next = head_2
            head_1 = head_2

        while head_1:
            s = head_1.val + e
            mod = s % 10
            e = s // 10
            head_1.val = mod
            tail = head_1
            head_1 = head_1.next

        if e:
            tail.next = ListNode(e)

        return l1
            
            