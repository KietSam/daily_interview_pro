import unittest


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def preorder(self):
        print(self.value + " ", end="")
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()


def invert(node):
    if node is None:
        return
    node.left = invert(node.left)
    node.right = invert(node.right)
    tmp = node.left
    node.left = node.right
    node.right = tmp
    return node


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')

root.preorder()
# a b d e c f
print("\n")
invert(root)
root.preorder()
# a c f b e d


# class BoilerplateTest(unittest.TestCase):
#
#     def setUp(self):
#         pass
#
#     def test1(self):
#         # expected, actual
#         # self.assertEqual([1, 4], self.solution.getRange([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 2))
#         pass
#
#
# def main():
#     unittest.main()
#
#
# if __name__ == '__main__':
#     main()
