
import pytest
from common_setup import run_test

def test_correct_username_correct_password():
    run_test("correct_username_correct_password", "Correct username and correct password prints \"Welcome\"", "Expected 'Welcome' message for valid credentials.")

if __name__ == '__main__':
    pytest.main()