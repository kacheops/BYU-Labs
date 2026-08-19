import pytest
from common_setup import pre_test_setup, check_internet_connection

def test_program_finishes_without_errors():
    test_outputs, test_points_awarded, test_feedback, test_response_data = pre_test_setup("program_finishes_without_errors")
    if check_internet_connection():
        assert test_response_data['totalPointsAwarded'] == test_response_data['totalPointsPossible'], test_feedback
    else:
        output = test_outputs["program_finishes_without_errors"]
        assert "The program did not finish successfully due to EOFError" not in output

if __name__ == '__main__':
    pytest.main()
