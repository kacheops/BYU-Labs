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
    run_single_test,# this function is called by the test files that import it from this file: common_setup.py
)

program_name = 'first_program.py'

def run_test(test_name, test_description, error_message):
    run_single_test(test_name, test_description, error_message, pre_test_setup)

def logic_greeting():
    """Logic to test if the program displays a greeting message."""
    return run_program(['John', 'New York'], program_name)

def logic_name():
    """Logic to test if the program correctly includes the name in the output."""
    return run_program(['John', 'New York'], program_name)

def logic_city():
    """Logic to test if the program correctly includes the city in the output."""
    return run_program(['John', 'New York'], program_name)

def logic_message():
    """Logic to test if the final printed message is longer than the combined length of name and city."""
    return run_program(['John', 'New York'], program_name)


def pre_test_setup(test_name=None):
    test_outputs = {}
    test_points_awarded = {}
    test_feedback = ""
    test_response_data = None

    if test_name:
        if test_name == "greeting":
            test_outputs["greeting"] = logic_greeting()
        elif test_name == "name":
            test_outputs["name"] = logic_name()
        elif test_name == "city":
            test_outputs["city"] = logic_city()
        elif test_name == "message":
            test_outputs["message"] = logic_message()
    else:
        test_outputs = {
            "greeting": logic_greeting(),
            "name": logic_name(),
            "city": logic_city(),
            "message": logic_message()
        }

    if check_internet_connection():
        try:
            # Read the contents of the files
            with open('first_program.py', 'r') as f:
                student_code = f.read()
            with open('tests/test_first_program.py', 'r') as f:
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


