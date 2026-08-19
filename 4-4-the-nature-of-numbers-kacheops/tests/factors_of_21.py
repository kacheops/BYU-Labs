# test_odd_number.py
import pytest
from common_setup import pre_test_setup, check_internet_connection
import json

def test_perfect_square():
    test_name="factors_of_21"
    test_outputs,test_points_awarded,test_feedback, test_response_data = pre_test_setup(test_name=test_name)
 
    output = test_outputs["factors_of_21"]
    if check_internet_connection():
        # the string below comes from the autograding.json test, in the name field:
        assert test_points_awarded.get("Student correctly identifies the factors of 21", 0) == 2, test_feedback
    else:     
        assert "1,3,7,21" in output, "Factors of 21 are incorrect OR not printed as '1,3,7,21'."
if __name__ == '__main__':
    pytest.main()