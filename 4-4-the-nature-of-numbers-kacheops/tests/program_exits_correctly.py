# tests/program_exits_correctly.py
import pytest
from common_setup import pre_test_setup, check_internet_connection
import json

def test_program_exits_correctly():
    test_name = "program_exits_correctly"
    test_outputs, test_points_awarded, test_feedback, test_response_data = pre_test_setup(test_name=test_name)

    output = test_outputs[test_name]
    if check_internet_connection():
        assert test_points_awarded.get("Program exits correctly after 'N' input", 0) == 4, test_feedback
    else:
        assert "Thank you for playing!" in output, "Program does not exit correctly after 'N' input OR 'Thank you for playing!' is not printed."

if __name__ == '__main__':
    pytest.main()