
import pytest
from common_setup import run_test

def test_correct_username_incorrect_password():
    run_test("correct_username_incorrect_password", "Correct username AND incorrect password prints \"Invalid credentials\"", "Expected 'Invalid credentials' for invalid password.")

if __name__ == '__main__':
    pytest.main()