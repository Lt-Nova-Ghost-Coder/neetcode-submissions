# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head
        if not self.head:
            return None
        
        storing = []
        temp = self.head
        while temp:
            storing.append(temp.val)
            temp = temp.next
        
        n = len(storing)
        for i in range(len(storing) // 2):
            storing[i], storing[n - i - 1] = storing[n - i - 1], storing[i]
        
        index = 0
        temp = self.head
        while temp:
            temp.val = storing[index]
            index += 1
            temp = temp.next
        return self.head


        