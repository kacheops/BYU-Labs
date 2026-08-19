import pytest
from common_setup import run_test

def test_message():
    
    # the first parameter is the name of the test file in /tests
    # the second parameter is the name of the test in autograding.json
    # the third parameter is the error message to display if the test fails
    run_test("message", "Create Final Message", "There is no message printed after asking the user their name and birth city")

if __name__ == '__main__':
    pytest.main()

