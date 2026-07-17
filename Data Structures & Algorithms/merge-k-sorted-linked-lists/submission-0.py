# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.lists = lists
        array = []
        for lst in self.lists:
            while lst:
                array.append(lst.val)
                lst = lst.next
        if not array:
            return None
        array.sort()
        head = ListNode(array[0])
        temp = head
        for i in range(1, len(array)):
            x = ListNode(array[i])
            temp.next = x
            temp = temp.next
        return head
        