class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverseIteratively(self, head):
        itr_node = head.next
        head.next = None
        while itr_node is not None:
            tmp = itr_node.next
            itr_node.next = head
            head = itr_node
            itr_node = tmp

        return head

    # Recursive Solution
    def reverseRecursively(self, head):
        self.helper(None, head)

    def helper(self, head, itr):
        if itr is None:
            return
        else:
            tmp = itr.next
            itr.next = head
            self.helper(itr, tmp)



# Implement this.

# Test Program
# Initialize the test list:
testHead = ListNode(4)
testTail = testHead
# node1 = ListNode(3)
# testHead.next = node1
# node2 = ListNode(2)
# node1.next = node2
# node3 = ListNode(1)
# node2.next = node3
# testTail = ListNode(0)
# node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
# testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()


# 0 1 2 3 4