# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        current1 = list1
        current2 = list2

        dummy = ListNode()
        current = dummy

        if current1 is not None:
            print(current1.val)

        if current2 is not None:
            print(current2.val)

        while current1 is not None and current2 is not None:      
            
            if current1.val < current2.val:
                current.next = current1
                current1 = current1.next
                current = current.next

            else:
                current.next = current2
                current2 = current2.next
                current = current.next

        current.next = current1 if current1 is not None else current2

        return dummy.next
            