# test_odd_number.py
import pytest
from common_setup import pre_test_setup, check_internet_connection
import json

def test_non_pefect_square():
    test_name="non_perfect_square"
    test_outputs,test_points_awarded,test_feedback, test_response_data = pre_test_setup(test_name=test_name)
 
    output = test_outputs["non_perfect_square"]
    if check_internet_connection():
        # the string below comes from the autograding.json test, in the name field:
        assert test_points_awarded.get("Student prints 'x does not have a perfect square root' for non-perfect squares", 0) == 2, test_feedback
    else:     
        assert "8 does not have a perfect square root." in output, "Expected full output '8 does not have a perfect square root.' not printed."
if __name__ == '__main__':
    pytest.main()