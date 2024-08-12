from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        current_sum_node = dummy
        current = head.next  

        while current:
            current_sum = 0
            while current and current.val != 0:
                current_sum += current.val
                current = current.next
            if current_sum > 0:
                current_sum_node.next = ListNode(current_sum)
                current_sum_node = current_sum_node.next
            if current:
                current = current.next  

        return dummy.next




    head = [0,1,0,3,0,2,2,0]
    mergeNodes(head)

