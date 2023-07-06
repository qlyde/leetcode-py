# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head = ListNode()
        # curr = head
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         curr.next = ListNode(list1.val)
        #         list1 = list1.next
        #     else:
        #         curr.next = ListNode(list2.val)
        #         list2 = list2.next
        #     curr = curr.next

        # if list1:
        #     curr.next = list1
        # elif list2:
        #     curr.next = list2

        # return head.next
        if not list1:
            return list2
        if not list2:
            return list1
        l1 = list1.val < list2.val
        n = ListNode(list1.val if l1 else list2.val)
        n.next = self.mergeTwoLists(
            list1.next if l1 else list1, 
            list2 if l1 else list2.next
        )
        return n
