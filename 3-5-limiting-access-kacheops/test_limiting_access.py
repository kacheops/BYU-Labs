# *****************************************************************************
# *                                                                           *
# *   IMPORTANT: DO NOT MODIFY THIS FILE                                      *
# *                                                                           *
# *   This testing file is provided to help you check the functionality of    *
# *   your code and understand the requirements for this assignment.          *
# *                                                                           *
# *   Please review the tests carefully to understand what is expected, but   *
# *   DO NOT make any changes to this file. Modifying this file will          *
# *   interfere with the grading system, lead to incorrect results, and       *
# *   will be flagged as cheating.                                            *
# *                                                                           *
# *   Focus on writing your own code to meet the requirements outlined in the *
# *   tests.                                                                  *
# *                                                                           *
# *****************************************************************************

import subprocess
import pytest
import requests
import json
import socket
from tests.common_setup import pre_test_setup, check_internet_connection

test_outputs = {}
test_name = None
test_points_awarded = {}
test_response_data = {}

def test_all():
    test_outputs, test_points_awarded, test_feedback, test_response_data = pre_test_setup()  # passing no tests means test everything
    if check_internet_connection():
        assert test_response_data['totalPointsAwarded'] == test_response_data['totalPointsPossible'], test_feedback
    else:
        output = test_outputs["correct_username_correct_password"]
        assert "welcome" in output.lower(), "Expected 'Welcome' message for valid credentials."

        output = test_outputs["incorrect_username_correct_password"]
        assert "invalid credentials" in output.lower(), "Expected 'Invalid credentials' for invalid username."

        output = test_outputs["correct_username_incorrect_password"]
        assert "invalid credentials" in output.lower(), "Expected 'Invalid credentials' for invalid password."

        output = test_outputs["incorrect_username_incorrect_password"]
        assert "invalid credentials" in output.lower(), "Expected 'Invalid credentials' for invalid username and password."

        output = test_outputs["program_finish"]
        assert output.strip() != "", "The program did not finish successfully."

if __name__ == '__main__':
    pytest.main()