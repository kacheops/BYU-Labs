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

import os
import subprocess
import pytest
from common_setup import pre_test_setup, check_internet_connection
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(script_dir, '..', 'app.py')

# Define the command to execute your Python script
command = ["python", "app.py"]

def gather_data(file_path):
    """Read the contents of a file and extract the list of dictionaries."""
    data_list = []
    start_reading = False

    with open(file_path, 'r') as f:
        for line in f:
            # One line
            if line.strip().startswith("data") and line.strip().endswith("]"):
                # Extract the JSON string from the line
                json_str = line[line.index('['):line.rindex(']') + 1]
                # Parse the JSON string into a list of dictionaries
                data_list = json.loads(json_str)
                break
            #     Multiple lines
            else:
                 if line.strip().startswith("data"):
                    start_reading = True
                    continue
                 if start_reading:
                    if line.strip() == "]":
                        break
                    data_list.append(line.strip())

    return data_list


def test_all():
    test_outputs, test_points_awarded, test_feedback, test_response_data = pre_test_setup()  # passing no tests means test everything
    if check_internet_connection():
        assert test_response_data['totalPointsAwarded'] == test_response_data['totalPointsPossible'], test_feedback
    else:
        ##Asserts for test "correct_api_response"
        data = gather_data(app_path)
        assert len(data) >= 10, "Please ensure that your are pasting all of your api response data into the app.py file."

if __name__ == "__main__":
    pytest.main()
