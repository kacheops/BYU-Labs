import pytest
from common_setup import run_test

def test_greeting():
    
    # the first parameter is the name of the test file in /tests
    # the second parameter is the name of the test in autograding.json
    # the third parameter is the error message to display if the test fails
    run_test("greeting", "Greeting Message", "The program doesn't greet the user with a message when it starts")

if __name__ == '__main__':
    pytest.main()

