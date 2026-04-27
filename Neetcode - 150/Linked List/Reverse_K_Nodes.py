# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head

        # Step 2: reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # Step 3: connect to recursion
        head.next = self.reverseKGroup(curr, k)
        return prev


