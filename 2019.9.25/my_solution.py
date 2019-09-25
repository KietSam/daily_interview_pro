import unittest

def helper(seq, i):
    nums = set()
    for j in range(i, len(seq)):
        nums.add(seq[j])
        if len(nums) > 2:
            return j - i
    return len(seq) - i

def findSequence(seq):
    min_seq_length = 0
    for i in range(len(seq)):
        min_seq_length = max(min_seq_length, helper(seq, i))
    return min_seq_length



class BoilerplateTest(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        # expected, actual
        self.assertEqual(4, findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
        self.assertEqual(6, findSequence([1, 3, 5, 3, 1, 3, 1, 5, 5, 5, 5, 1]))
        self.assertEqual(0, findSequence([]))
        self.assertEqual(2, findSequence([1, 2]))
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
