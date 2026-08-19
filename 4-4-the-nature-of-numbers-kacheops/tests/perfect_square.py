# test_odd_number.py
import pytest
from common_setup import pre_test_setup, check_internet_connection
import json

def test_perfect_square():
    test_name="perfect_square"
    test_outputs,test_points_awarded,test_feedback, test_response_data = pre_test_setup(test_name=test_name)
 
    output = test_outputs["perfect_square"]
    if check_internet_connection():
        # the string below comes from the autograding.json test, in the name field:
        assert test_points_awarded.get("Student prints 'x has a perfect square root' for perfect squares", 0) == 2, test_feedback
    else:     
        assert "9 has a perfect square root." in output, "Expected full output '9 has a perfect square root.' not printed."
if __name__ == '__main__':
    pytest.main()