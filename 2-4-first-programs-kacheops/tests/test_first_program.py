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
from common_setup import pre_test_setup, check_internet_connection

test_outputs = {}
test_name = None
test_points_awarded = {}
test_response_data = {}

# This script runs ALL tests -- if you want to run separate tests, see the .tests folder
# This test has 1,233 tokens calling OpenAI gtp-4o model which costs $2.50 for 1 million tokens
# So it should cost $.004 or about half a penny for each time they run all test here using pytest

# In GitHub it runs each test separately which calls the API 8 times, so it will cost about $.032 each time they push their code

def test_all():
    test_outputs,test_points_awarded,test_feedback,test_response_data = pre_test_setup()# passing no tests means test everything
    if check_internet_connection():
        assert test_response_data['totalPointsAwarded'] == test_response_data['totalPointsPossible'], test_feedback

    else :
        output = test_outputs["greeting"]
        assert output.strip() != "", "The program doesn't greet the user with a message when it starts"

        output = test_outputs["name"]
        assert "John" in output.strip(), "The program doesn't greet the user by their name"

        output = test_outputs["city"]
        assert "New York" in output.strip(), "The program doesn't talk about the city the user is from in the message, ex: ...Chicago is a nice city..."

        output = test_outputs["message"]
        assert output.strip() !="", "There is no message printed after asking the user their name and birth city"

if __name__ == '__main__':
    pytest.main()