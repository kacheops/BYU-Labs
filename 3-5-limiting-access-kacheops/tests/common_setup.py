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

program_name = 'limiting_access.py'

def run_test(test_name, test_description, error_message):
    run_single_test(test_name, test_description, error_message, pre_test_setup)

# Test scenarios with different input combinations
def logic_correct_username_correct_password():
    """Test with correct username and correct password"""
    return run_program(['admin', 'password123'], program_name)  # Adjust with actual credentials

def logic_correct_username_incorrect_password():
    """Test with correct username but incorrect password"""
    return run_program(['admin', 'wrongpass'], program_name)

def logic_incorrect_username_correct_password():
    """Test with incorrect username but correct password"""
    return run_program(['wronguser', 'password123'], program_name)

def logic_incorrect_username_incorrect_password():
    """Test with incorrect username and incorrect password"""
    return run_program(['wronguser', 'wrongpass'], program_name)

def logic_program_finish():
    """Test if the program completes successfully"""
    return run_program(['admin', 'password123'], program_name)

def pre_test_setup(test_name=None):
    test_outputs = {}
    test_points_awarded = {}
    test_feedback = ""
    test_response_data = None

    if test_name:
        if test_name == "correct_username_correct_password":
            test_outputs["correct_username_correct_password"] = logic_correct_username_correct_password()
        elif test_name == "correct_username_incorrect_password":
            test_outputs["correct_username_incorrect_password"] = logic_correct_username_incorrect_password()
        elif test_name == "incorrect_username_correct_password":
            test_outputs["incorrect_username_correct_password"] = logic_incorrect_username_correct_password()
        elif test_name == "incorrect_username_incorrect_password":
            test_outputs["incorrect_username_incorrect_password"] = logic_incorrect_username_incorrect_password()
        elif test_name == "program_finish":
            test_outputs["program_finish"] = logic_program_finish()
    else:
        test_outputs = {
            "correct_username_correct_password": logic_correct_username_correct_password(),
            "correct_username_incorrect_password": logic_correct_username_incorrect_password(),
            "incorrect_username_correct_password": logic_incorrect_username_correct_password(),
            "incorrect_username_incorrect_password": logic_incorrect_username_incorrect_password(),
            "program_finish": logic_program_finish()
        }

    if check_internet_connection():
        try:
            # Read the contents of the files
            with open('limiting_access.py', 'r') as f:
                student_code = f.read()
            with open('test_limiting_access.py', 'r') as f:
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