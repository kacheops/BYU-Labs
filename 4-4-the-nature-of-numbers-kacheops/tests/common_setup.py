# common_setup.py
import subprocess
import requests
import json
import socket
import os
import platform
import sys
sys.path.append('..')
from central_setup.central_setup import (
    execute_logic,
    check_internet_connection,
    run_program,
    run_single_test,  # this function is called by the test files that import it from this file: common_setup.py
)

program_name='nature_of_numbers.py'

def run_test(test_name, test_description, error_message):
    run_single_test(test_name, test_description, error_message, pre_test_setup)

# Test functions for different number scenarios
def logic_even_number():
    """Test with an even number input."""
    return run_program(['4', 'n'], program_name)

def logic_odd_number():
    """Test with an odd number input."""
    return run_program(['5', 'n'],program_name)

def logic_perfect_square():
    """Test with a perfect square input."""
    return run_program(['9', 'n'],program_name)

def logic_non_perfect_square():
    """Test with a non-perfect square input."""
    return run_program(['10', 'n'],program_name)

def logic_factors_of_9():
    """Test with a number that has specific factors (9)."""
    return run_program(['9', 'n'],program_name)

def logic_factors_of_21():
    """Test with a number that has specific factors (21)."""
    return run_program(['21', 'n'],program_name)

def logic_program_prompts_for_another_input():
    """Test if the program prompts for another number."""
    return run_program(['10', 'y', '15', 'n'],program_name)

def logic_program_exits_correctly():
    """Test if the program exits correctly when user chooses not to continue."""
    return run_program(['10', 'n'],program_name)

def pre_test_setup(test_name=None):
    test_outputs = {}
    test_points_awarded = {}
    test_feedback = ""
    test_response_data = None

    if test_name:
        if test_name == "even_number":
            test_outputs["even_number"] = logic_even_number()
        elif test_name == "odd_number":
            test_outputs["odd_number"] = logic_odd_number()
        elif test_name == "perfect_square":
            test_outputs["perfect_square"] = logic_perfect_square()
        elif test_name == "non_perfect_square":
            test_outputs["non_perfect_square"] = logic_non_perfect_square()
        elif test_name == "factors_of_9":
            test_outputs["factors_of_9"] = logic_factors_of_9()
        elif test_name == "factors_of_21":
            test_outputs["factors_of_21"] = logic_factors_of_21()
        elif test_name == "program_prompts_for_another_input":
            test_outputs["program_prompts_for_another_input"] = logic_program_prompts_for_another_input()
        elif test_name == "program_exits_correctly":
            test_outputs["program_exits_correctly"] = logic_program_exits_correctly()
    else:
        test_outputs = {
            "even_number": logic_even_number(),
            "odd_number": logic_odd_number(),
            "perfect_square": logic_perfect_square(),
            "non_perfect_square": logic_non_perfect_square(),
            "factors_of_9": logic_factors_of_9(),
            "factors_of_21": logic_factors_of_21(),
            "program_prompts_for_another_input": logic_program_prompts_for_another_input(),
            "program_exits_correctly": logic_program_exits_correctly()
        }

    if check_internet_connection():
        try:
            # Read the contents of the files
            with open('nature_of_numbers.py', 'r') as f:
                student_code = f.read()
            with open('test_nature_of_numbers.py', 'r') as f:
                pytest_code = f.read()
            with open('.github/classroom/autograding.json', 'r') as f:
                autograding_config = json.load(f)

            # Pass the logic to the central_setup module
            test_outputs, test_points_awarded, test_feedback, test_response_data = execute_logic(
                test_name, test_outputs, student_code, pytest_code, autograding_config
            )

        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print(f"API call failed: {e}")
            print("Proceeding without API response. Run the test again with a working API to receive more user-friendly feedback.")

    return test_outputs, test_points_awarded, test_feedback, test_response_data