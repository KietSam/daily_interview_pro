import unittest


def helper(exp, start_index, end_index, paren_args):
    if end_index < start_index:
        return
    if exp[start_index] == '+':
        return + helper(exp, start_index + 1, end_index, paren_args)
    if exp[start_index] == '-':
        return - helper(exp, start_index + 1, end_index, paren_args)
    if exp[start_index] == '(':
        paren_args.append(None)
        return helper(exp, start_index + 1, end_index, paren_args)

    pass


def eval(expression):
    # Fill this in.
    exp_array = expression.split(" ")
    print(exp_array)
    return helper(exp_array, 0, len(exp_array) - 1, [])



class BoilerplateTest(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        # expected, actual
        self.assertEqual(-4, eval('- ( 3 + ( 2 - 1 ) )'))
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
