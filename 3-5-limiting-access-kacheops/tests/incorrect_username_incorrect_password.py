
import pytest
from common_setup import run_test

def test_incorrect_username_incorrect_password():
    run_test("incorrect_username_incorrect_password", "Incorrect username AND incorrect password prints \"Invalid credentials\"", "Expected 'Invalid credentials' for invalid username and password.")

if __name__ == '__main__':
    pytest.main()