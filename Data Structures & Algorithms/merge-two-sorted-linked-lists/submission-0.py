# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.list1 = list1
        self.list2 = list2
        
        if not self.list1 and not self.list2:
            return None
        if not self.list1:
            return self.list2
        if not self.list2:
            return self.list1

        newList = ListNode(0)
        temp1 = self.list1
        temp2 = self.list2
        dummy = newList

        while temp1 and temp2:
            if temp1.val > temp2.val:
                x = ListNode(temp2.val)
                temp2 = temp2.next
            else:
                x = ListNode(temp1.val)
                temp1 = temp1.next
            dummy.next = x
            dummy = dummy.next
        
        if not temp1:
            dummy.next = temp2
        if not temp2:
            dummy.next = temp1
        
        return newList.next

        