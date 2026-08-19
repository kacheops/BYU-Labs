
import pytest
from common_setup import run_test

def test_incorrect_username_correct_password():
    run_test("incorrect_username_correct_password", "Incorrect username AND correct password prints \"Invalid credentials\"", "Expected 'Invalid credentials' for invalid username.")

if __name__ == '__main__':
    pytest.main()