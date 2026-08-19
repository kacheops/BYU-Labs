
import pytest
from common_setup import run_test

def test_print_statement():
    # the first parameter is the name of the test file in /tests
    # the second parameter is the name of the test in autograding.json
    # the third parameter is the error message to display if the test fails
    run_test("print_statement", "Create Final Message", "The program doesn't mention diameter, circumference, or area in the output")

if __name__ == '__main__':
    pytest.main()