import unittest
from timeout_decorator import timeout
from colorama import Fore, Style, init
from problem import Solution

locateBook = Solution.locateBook

# Initialize colorama
init(autoreset=True)

class TestExample(unittest.TestCase):

    def run_test(self, input_values, expected_value):
        solution = Solution()

        try:
            self.assertEqual(locateBook(solution, *input_values), expected_value)
        except TimeoutError:
            self.fail()

    @timeout(2)
    def test_case_1(self):
        self.run_test([[2, 4, 6, 8, 10],8], 3)
    
    @timeout(2)
    def test_case_2(self):
        self.run_test([[3, 5, 7, 9, 15],10], -1)

    ##test for extremely large test cases and negative
    @timeout(.01)
    def test_case_3(self):
        self.run_test([[-6,-5,-2,-3, -1, 3, 5, 7, 9, 15,16,20,40,60,80,99,100,101,102,103,104,105,106,107,108,109],-6], 0)
        
    def tearDown(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        if not result.wasSuccessful():
            print(f"{Fore.RED}{self._testMethodName} FAILED{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}{self._testMethodName} PASSED{Style.RESET_ALL}")


if __name__ == '__main__':
    unittest.main()