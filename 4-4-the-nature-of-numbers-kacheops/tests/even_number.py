# test_odd_number.py
import pytest
from common_setup import pre_test_setup, check_internet_connection
import json


def test_even_number():
    test_name="even_number"
    test_outputs,test_points_awarded,test_feedback, test_response_data = pre_test_setup(test_name=test_name)
 
    output = test_outputs["even_number"]
    if check_internet_connection():
        # the string below comes from the autograding.json test, in the name field:
        assert test_points_awarded.get("Student prints 'x is an even number' for even inputs", 0) == 2, test_feedback
    else:     
        assert "4 is an even number." in output, "Expected full output '4 is an even number.' not found."
if __name__ == '__main__':
    pytest.main()