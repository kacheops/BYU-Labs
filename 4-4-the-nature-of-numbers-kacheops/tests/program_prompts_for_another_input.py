# tests/program_prompts_for_another_input.py
import pytest
from common_setup import pre_test_setup, check_internet_connection
import json

def test_program_prompts_for_another_input():
    test_name = "program_prompts_for_another_input"
    test_outputs, test_points_awarded, test_feedback, test_response_data = pre_test_setup(test_name=test_name)

    output = test_outputs[test_name]
    if check_internet_connection():
        assert test_points_awarded.get("Program prompts for another input after initial input", 0) == 4, test_feedback
    else:
        assert "Would you like to enter another number? (Y/N)" in output, "Program does not prompt for another input correctly."

if __name__ == '__main__':
    pytest.main()