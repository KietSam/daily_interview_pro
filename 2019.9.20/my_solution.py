import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.oldMax = None

    def getMax(self):
        if self.oldMax is None:
            return self.val
        return max(self.oldMax.val, self.val)

    def getMaxNode(self):
        if self.oldMax is None:
            return self
        else:
            if self.val >= self.oldMax.val:
                return self
            else:
                return self.oldMax

class MaxStack:
    def __init__(self):
        self.top = None
        pass

    def push(self, val):
        node = Node(val)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            node.oldMax = self.top.getMaxNode()
            self.top = node

    def pop(self):
        if self.top is None:
            raise NotImplemented
        else:
            val = self.top.val
            self.top = self.top.next
            return val

    def max(self):
        if self.top is None:
            raise NotImplemented
        else:
            return self.top.getMax()


class BoilerplateTest(unittest.TestCase):

    def test1(self):
        s = MaxStack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(2)
        self.assertEqual(3, s.max())
        self.assertEqual(2, s.pop())
        self.assertEqual(3, s.pop())
        self.assertEqual(2, s.max())

    def test2(self):
        s = MaxStack()
        s.push(3)
        s.push(10)
        s.push(5)
        s.push(8)
        self.assertEqual(10, s.max())
        self.assertEqual(8, s.pop())
        self.assertEqual(10, s.max())
        self.assertEqual(5, s.pop())
        self.assertEqual(10, s.max())
        self.assertEqual(10, s.pop())
        self.assertEqual(3, s.max())
        self.assertEqual(3, s.pop())

    def test3(self):
        s = MaxStack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(5)
        s.push(8)
        s.push(4)
        s.push(47)
        self.assertEqual(47, s.max())
        self.assertEqual(47, s.pop())
        self.assertEqual(8, s.max())
        self.assertEqual(4, s.pop())
        self.assertEqual(8, s.max())
        self.assertEqual(8, s.pop())
        self.assertEqual(5, s.max())
        self.assertEqual(5, s.pop())
        self.assertEqual(3, s.max())
        self.assertEqual(3, s.pop())
        self.assertEqual(2, s.max())
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.max())
        self.assertEqual(1, s.pop())


def main():
    unittest.main()


if __name__ == '__main__':
    main()
