# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        return self.helper(l1, l2, 0)

    def helper(self, l1, l2, carry_over):
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            l1 = ListNode(0)
        elif l2 is None:
            l2 = ListNode(0)
        new_sum = l1.val + l2.val + carry_over
        new_node = ListNode(new_sum % 10)
        new_node.next = self.helper(l1.next, l2.next, new_sum // 10)
        return new_node


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8
