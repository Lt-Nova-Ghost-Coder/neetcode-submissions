# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        self.head = head
        self.left = left
        self.right = right

        array = []
        temp = self.head
        while temp:
            array.append(temp.val)
            temp = temp.next
        
        l = self.left - 1
        r = self.right - 1

        while l < r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1
        
        i = 0
        temp = self.head
        while temp:
            temp.val = array[i]
            i += 1
            temp = temp.next
        return self.head
        