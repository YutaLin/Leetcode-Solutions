# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        prev = None
        cur = slow

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        head_r = prev
        head_l = head
        while head_r.next:
            r_nxt = head_r.next
            l_nxt = head_l.next
            
            head_l.next = head_r
            head_r.next = l_nxt
            
            head_l = l_nxt
            head_r = r_nxt

        return head