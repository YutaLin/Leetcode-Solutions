# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        p = head
        while p:
            p = p.next
            n += 1

        dummy = ListNode(next=head)
        p0 = dummy
        prev = None
        cur = head

        while n >= k:
            
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            n -= k
            
            nxt = p0.next
            p0.next.next = cur
            p0.next = prev
            p0 = nxt
        return dummy.next
        

# (1 -> 2) -> 3 -> 4 -> 5
# (2 -> 1) 1. remember next rev_head

# p0 -> 1 -> 2 -> 3 -> 4 -> 5
# p0 -> 1 <- 2    3 -> 4 -> 5
#           prev  cur           
# nxt = p0.next
# p0.next.next = cur
# p0.next = prev
# p0. nxt
