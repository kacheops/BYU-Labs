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

program_name = 'putting_python_to_work.py'

def run_test(test_name, test_description, error_message):
    run_single_test(test_name, test_description, error_message, pre_test_setup)

def logic_diameter():
    """Logic to test if the program calculates the diameter correctly."""
    return run_program(['5'], program_name)

def logic_circumference():
    """Logic to test if the program calculates the circumference correctly."""
    return run_program(['5'], program_name)

def logic_area():
    """Logic to test if the program calculates the area correctly."""
    return run_program(['5'], program_name)

def logic_print_statement():
    """Logic to test if the final printed message contains diameter, circumference, and area."""
    return run_program(['5'], program_name)

def pre_test_setup(test_name=None):
    test_outputs = {}
    test_points_awarded = {}
    test_feedback = ""
    test_response_data = None

    if test_name:
        if test_name == "diameter":
            test_outputs["diameter"] = logic_diameter()
        elif test_name == "circumference":
            test_outputs["circumference"] = logic_circumference()
        elif test_name == "area":
            test_outputs["area"] = logic_area()
        elif test_name == "print_statement":
            test_outputs["print_statement"] = logic_print_statement()
    else:
        test_outputs = {
            "diameter": logic_diameter(),
            "circumference": logic_circumference(),
            "area": logic_area(),
            "print_statement": logic_print_statement()
        }

    if check_internet_connection():
        try:
            # Read the contents of the files
            with open('putting_python_to_work.py', 'r') as f:
                student_code = f.read()
            with open('test_putting_python_to_work.py', 'r') as f:
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