# Last updated: 5/8/2025, 2:40:04 PM
'''
1. Find second half of list with slow fast pointer
2. reverse second half of list
3. merge two list
Time: O(n)
Space: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow_p = head
        fast_p = head
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        # reverse link
        prev, curr = None, slow_p
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # merge link
        first, second = head, prev
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp
            
            tmp = second.next
            second.next = first
            second = tmp
        return head
            
        
        
        
# 1 -> 3 -> 4 -> 6
# 1 -> 6 -> 3 -> 4

# find second half of list
# reverse second half of list
# concatnate two lists