import unittest

class Solution:

    def get_leftmost_index(self, arr, target):
        if len(arr) == 0:
            return None
        low = 0
        high = len(arr)

        while low < high:
            mid = (low + high) // 2
            if target <= arr[mid]:
                high = mid
            else:
                low = mid + 1

        if low >= len(arr) or arr[low] != target:
            return None
        return low


    def getRange(self, arr, target):
        low = self.get_leftmost_index(arr, target)
        high = low

        if low is None:
            return [-1, -1]

        while high < len(arr) and arr[high] == target:
            high += 1

        return [low, high-1]



    def getRangeLinear(self, arr, target):
        # Space: O(1)
        # Runtime: O(n)
        mapping = {}
        for i, num in enumerate(arr):
            if num == target:
                if target in mapping:
                    mapping[target][1] = i
                else:
                    mapping[target] = [i, i]
            elif num > target:
                break
        if target in mapping:
            return mapping[target]
        return [-1, -1]



class BoilerplateTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test1(self):
        self.assertEqual([1, 4], self.solution.getRange([1, 2, 2, 2, 2, 3, 4, 7, 8, 8], 2))
        self.assertEqual([6, 8], self.solution.getRange([1,3,3,5,7,8,9,9,9,15], 9))
        self.assertEqual([1, 2], self.solution.getRange([100, 150, 150, 153], 150))
        self.assertEqual([0, 0], self.solution.getRange([1], 1))
        self.assertEqual([-1,-1], self.solution.getRange([1,2,3,4,5,6,7,8,10], 9))
        self.assertEqual([-1,-1], self.solution.getRange([1], 9))
        pass

    def test2(self):
        self.assertEqual([0, 0], self.solution.getRange([1], 1))
        pass



def main():
    unittest.main()

if __name__ == '__main__':
    main()