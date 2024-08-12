class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        dummmy = ListNode()
        current = dummmy
        carry =0

        while l1 is not None or l2 is not None or carry!=0:
            val1=l1.val if l1 is not None else 0
            val2=l2.val if l2 is not None else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummmy.next