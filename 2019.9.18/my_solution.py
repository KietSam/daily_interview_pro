import unittest


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root, k, floor=None, ceil=None):
    if root == None:
        return floor, ceil
    if k == root.value:
        return k, k
    if k < root.value:
        return findCeilingFloor(root.left, k, floor=floor, ceil=root.value)
    if k > root.value:
        return findCeilingFloor(root.right, k, floor=root.value, ceil=ceil)

class BoilerplateTest(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        root = Node(8)
        root.left = Node(4)
        root.right = Node(12)

        root.left.left = Node(2)
        root.left.right = Node(6)

        root.right.left = Node(10)
        root.right.right = Node(14)


        self.assertEqual(findCeilingFloor(root, 5), (4, 6))

    def test2(self):
        root = Node(8)
        root.left = Node(4)
        root.right = Node(12)

        root.left.left = Node(2)
        root.left.right = Node(6)

        root.right.left = Node(10)
        root.right.right = Node(14)
        self.assertEqual(findCeilingFloor(root, 15), (14, None))

    def test3(self):
        root = Node(8)
        root.left = Node(4)
        root.right = Node(12)

        root.left.left = Node(2)
        root.left.right = Node(6)

        root.right.left = Node(10)
        root.right.right = Node(14)
        self.assertEqual(findCeilingFloor(root, 1), (None, 2))

    def test4(self):
        root = Node(8)
        root.left = Node(4)
        root.right = Node(12)

        root.left.left = Node(2)
        root.left.right = Node(6)

        root.right.left = Node(10)
        root.right.right = Node(14)
        self.assertEqual(findCeilingFloor(root, 4), (4, 4))

def main():
    unittest.main()


if __name__ == '__main__':
    main()
