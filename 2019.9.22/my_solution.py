import unittest


def findPythagoreanTriplets(nums):
    # Fill this in.
    squares = set(num * num for num in nums)
    for i, a in enumerate(squares):
        for j, b in enumerate(squares):
            if i != j and (a + b) in squares:
                return True
    return False


class BoilerplateTest(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        self.assertTrue(findPythagoreanTriplets([3, 12, 5, 13]))
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
