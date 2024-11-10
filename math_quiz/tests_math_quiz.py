import unittest
from math_quiz.math_quiz import select_random_integer_func, select_random_opertaor_func, get_problem_and_output


class TestMathGame(unittest.TestCase):

    def test_select_random_integer_func(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = select_random_integer_func(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_random_opertaor_func(self):
        # Test if operator generated is '+', '-' or '*'
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test large number of times
            random_operator = select_random_opertaor_func()
            self.assertIn(random_operator, operators)

        pass

    def test_get_problem_and_output(self):
        # Test if questions and answers generated are correct

        # test case format (left operand, right operand, operator, expected_problem, expected_answer)
        test_cases = [
            (3, 2, '+', '3 + 2', 5),
            (7, 1, '-', '7 - 1', 6),
            (9, 5, '*', '9 * 5', 45),
            (-5, 0, '+', '-5 + 0', -5),
            (4, 2, '-', '4 - 2', -2),
            (-3,-4, '*', '-3 * -4', 12),
            (-4, 2, '*', '-4 * 2', -8)
        ]

        # check if generated problem & answer matches to the expected problem & answer for each test case
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            generated_problem, generated_answer = get_problem_and_output(num1, num2, operator)
            self.assertListEqual([generated_problem, generated_answer], [expected_problem, expected_answer])



if __name__ == "__main__":
    unittest.main()
