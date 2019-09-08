import unittest
from .interview_code import *


class BoilerplateTest(unittest.TestCase):
    def test1(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        result = Solution().addTwoNumbers(l1, l2)
        expected = [7, 0, 8]
        i = 0
        while result:
            self.assertEqual(result.val, expected[i])
            result = result.next
            i += 1

    def test2(self):
        l1 = ListNode(3)
        l1.next = ListNode(4)

        l2 = ListNode(3)
        l2.next = ListNode(4)
        l2.next.next = ListNode(6)

        result = Solution().addTwoNumbers(l1, l2)
        expected = [6, 8, 6]
        i = 0
        while result:
            self.assertEqual(result.val, expected[i])
            result = result.next
            i += 1

    def test3(self):
        l1 = ListNode(3)

        l2 = ListNode(3)
        l2.next = ListNode(4)
        l2.next.next = ListNode(6)

        result = Solution().addTwoNumbers(l1, l2)
        expected = [6, 4, 6]
        i = 0
        while result:
            self.assertEqual(result.val, expected[i])
            result = result.next
            i += 1

    def test4(self):
        l1 = ListNode(9)

        l2 = ListNode(3)
        l2.next = ListNode(4)
        l2.next.next = ListNode(6)

        result = Solution().addTwoNumbers(l1, l2)
        expected = [2, 5, 6]
        i = 0
        while result:
            self.assertEqual(result.val, expected[i])
            result = result.next
            i += 1



def main():
    unittest.main()

if __name__ == '__main__':
    main()