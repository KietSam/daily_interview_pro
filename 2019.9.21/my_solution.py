import unittest



def staircase(n):
    mem = {}
    def helper(x):
        if x < 0:
            return 0
        if x == 0:
            return 1
        if x not in mem:
            mem[x] = helper(x - 1) + helper(x - 2)
        return mem[x]

    return helper(n)




class BoilerplateTest(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        # expected, actual
        # self.assertEqual([1, 4], self.solution.getRange([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 2))
        self.assertEqual(5, staircase(4))
        self.assertEqual(8, staircase(5))
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
