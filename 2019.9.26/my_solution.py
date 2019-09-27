import unittest

def find_cycle(graph):
    # Fill this in.
    return helper(graph, [])

def helper(graph, visited):
    for key in graph:
        if key in visited:
            return True
        visited.append(key)
        if helper(graph[key], visited):
            return True
    return False




class BoilerplateTest(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': {'a2': {}, 'a3': {}},
            'b': {'b2': {}},
            'c': {}
        }
        pass

    def test1(self):
        # expected, actual
        self.assertFalse(find_cycle(self.graph))
        pass

    def test2(self):
        # expected, actual
        self.graph['c'] = self.graph
        self.assertTrue(find_cycle(self.graph))
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
