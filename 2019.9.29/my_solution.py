import unittest

def helper(n, m, i, j):
    if i == n and j == m:
        return 1
    if i > n or j > m:
        return 0
    return helper(n, m, i + 1, j) + helper(n, m, i, j + 1)

def num_ways(n, m):
    return helper(n, m, 1, 1)



class BoilerplateTest(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        # expected, actual
        self.assertEqual(2, num_ways(2, 2))
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
