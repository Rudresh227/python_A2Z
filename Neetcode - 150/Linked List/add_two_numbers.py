#Brute Force
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = ""
        nums2 = ""

        curr = l1
        while curr:
            nums1 = str(curr.val) + nums1
            curr = curr.next

        curr = l2
        while curr:
            nums2 = str(curr.val) + nums2
            curr = curr.next

        nums1 = int(nums1)
        nums2 = int(nums2)

        result = nums1 + nums2

        result = str(result)

        dummy = ListNode(0)
        curr = dummy

        for char in reversed(result):
            curr.next = ListNode(int(char))
            curr = curr.next

        return dummy.next


#Optimal

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            val = total % 10

            curr.next = ListNode(val)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
