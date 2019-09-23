import unittest


def distance(s1: str, s2: str):
    return helper(s1, s2, 0, 0)

def helper(s1, s2, i1, i2):
    if i1 >= len(s1) and i2 >= len(s2):
        return 0
    if i1 >= len(s1):
        return len(s2) - i2
    if i2 >= len(s2):
        return len(s1) - i1
    elif s1[i1] == s2[i2]:
        return helper(s1, s2, i1+1, i2+1)
    else:
        return min(helper(s1, s2, i1+1, i2+1), helper(s1, s2, i1+1, i2), helper(s1, s2, i1, i2+1)) + 1


class BoilerplateTest(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        # expected, actual
        self.assertEqual(2, distance('biting', 'sitting'))

    def test2(self):
        self.assertEqual(7, distance('a', 'sitting'))

    def test2(self):
        self.assertEqual(3, distance('horse', 'ros'))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
