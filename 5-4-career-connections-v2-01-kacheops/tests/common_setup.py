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

program_name = 'accessAPI.py'

def run_test(test_name, test_description, error_message):
    run_single_test(test_name, test_description, error_message, pre_test_setup)

def logic_get_summary_valid_book_and_chapter():
    """Test if the program correctly retrieves summary for valid book and chapter."""
    return run_program(['1Nephi', '2'], program_name)

def logic_get_summary_invalid_book():
    """Test if the program handles invalid book inputs gracefully."""
    return run_program(['InvalidBook', '1'], program_name)

def logic_get_summary_invalid_chapter():
    """Test if the program handles invalid chapter inputs gracefully."""
    return run_program(['1Nephi', 'InvalidChapter'], program_name)

def logic_program_finishes_without_errors():
    """Test if the program completes successfully."""
    return run_program(['1Nephi', '2', 'n'], program_name)

def pre_test_setup(test_name=None):
    test_outputs = {}
    test_points_awarded = {}
    test_feedback = ""
    test_response_data = None

    # Resolve the base directory path
    base_dir = os.path.dirname(os.path.abspath(__file__))
    accessAPI_path = os.path.join(base_dir, '..', 'accessAPI.py')
    autograding_config_path = os.path.join(base_dir, '..', '.github', 'classroom', 'autograding.json')
    pytest_code_path = os.path.join(base_dir, 'test_accessAPI.py')

    if test_name:
        if test_name == "get_summary_valid_book_and_chapter":
            test_outputs["get_summary_valid_book_and_chapter"] = logic_get_summary_valid_book_and_chapter()
        elif test_name == "get_summary_invalid_book":
            test_outputs["get_summary_invalid_book"] = logic_get_summary_invalid_book()
        elif test_name == "get_summary_invalid_chapter":
            test_outputs["get_summary_invalid_chapter"] = logic_get_summary_invalid_chapter()
        elif test_name == "program_finishes_without_errors":
            test_outputs["program_finishes_without_errors"] = logic_program_finishes_without_errors()
    else:
        test_outputs = {
            "get_summary_valid_book_and_chapter": logic_get_summary_valid_book_and_chapter(),
            "get_summary_invalid_book": logic_get_summary_invalid_book(),
            "get_summary_invalid_chapter": logic_get_summary_invalid_chapter(),
            "program_finishes_without_errors": logic_program_finishes_without_errors()
        }

    if check_internet_connection():
        try:
            # Read the contents of the files
            with open(accessAPI_path, 'r') as f:
                student_code = f.read()
            with open(pytest_code_path, 'r') as f:
                pytest_code = f.read()
            with open(autograding_config_path, 'r') as f:
                autograding_config = json.load(f)

            # Pass the logic to the central_setup module
            test_outputs, test_points_awarded, test_feedback, test_response_data = execute_logic(
                test_name, test_outputs, student_code, pytest_code, autograding_config
            )

        except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
            print(f"API call failed: {e}")
            print("Proceeding without API response. Run the test again with a working API to receive more user-friendly feedback.")

    return test_outputs, test_points_awarded, test_feedback, test_response_data
