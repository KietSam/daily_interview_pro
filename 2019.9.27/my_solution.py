import unittest


def search_left_to_right(matrix, word, i, j):
    width = len(matrix[0])
    word_length = len(word)
    if j + word_length > width:
        return False
    for k in range(j, j + word_length):
        if matrix[i][j + k] != word[k]:
            return False
    return True

def search_top_to_bottom(matrix, word, i, j):
    height = len(matrix)
    word_length = len(word)
    if i + word_length > height:
        return False
    for k in range(i, i + word_length):
        if matrix[i + k][j] != word[k]:
            return False
    return True

def word_search(matrix, word):
    word_length = len(word)
    if word_length == 0:
        return True
    height = len(matrix)
    if height == 0:
        return False
    width = len(matrix[0])
    if width == 0:
        return False
    if height < word_length and width < word_length:
        return False

    for i in range(height):
        for j in range(width):
            if search_left_to_right(matrix, word, i, j):
                return True
            if search_top_to_bottom(matrix, word, i, j):
                return True
    return False



class BoilerplateTest(unittest.TestCase):

    def setUp(self):
        self.matrix = [
            ['F', 'A', 'C', 'I'],
            ['O', 'B', 'Q', 'P'],
            ['A', 'N', 'O', 'B'],
            ['M', 'A', 'S', 'S']]

        pass

    def test1(self):
        # expected, actual
        self.assertEqual(True, word_search(self.matrix, 'FOAM'))
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
