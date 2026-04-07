class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

#Actual Code
def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    curr.next = list1 if list1 else list2

    return dummy.next


print(to_list(mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))))  # [1, 1, 2, 3, 4, 4]
print(to_list(mergeTwoLists(build([]), build([]))))                 # []
print(to_list(mergeTwoLists(build([]), build([0]))))                # [0]
print(to_list(mergeTwoLists(build([1, 3, 5]), build([2, 4, 6]))))  # [1, 2, 3, 4, 5, 6]