import pytest
from common_setup import run_test

def test_city():

    # the first parameter is the name of the test file in /tests
    # the second parameter is the name of the test in autograding.json
    # the third parameter is the error message to display if the test fails
    run_test("city", "Request Birthplace From User", "The program doesn't talk about the city the user is from in the message, ex: ...Chicago is a nice city...")

if __name__ == '__main__':
    pytest.main()

