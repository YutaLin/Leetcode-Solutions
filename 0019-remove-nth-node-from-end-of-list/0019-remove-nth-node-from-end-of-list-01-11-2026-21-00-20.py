# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # total = 0
        # cur = head
        # while cur:
        #     cur = cur.next
        #     total += 1

        # dummy = ListNode(next=head)
        # cur = dummy
        # for _ in range(total - n):
        #     cur = cur.next
        # cur.next = cur.next.next

        # return dummy.next
        dummy = ListNode(next=head)
        fast = dummy
        for _ in range(n):
            fast = fast.next

        slow = dummy
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


# count number of nodes - n => node before deleted node
# dummy node -> first node (in case n would be node n)

# two pointer
# fast goes n, the we
