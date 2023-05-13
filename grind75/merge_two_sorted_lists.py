from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.merge_two_lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_two_lists(list1, list2.next)
            return list2


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    s = Solution()

    result = s.merge_two_lists(list1, list2)
