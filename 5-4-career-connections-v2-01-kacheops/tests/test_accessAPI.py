import pytest
from common_setup import pre_test_setup, check_internet_connection

test_outputs = {}
test_name = None
test_points_awarded = {}
test_response_data = {}

def test_all():
    test_outputs, test_points_awarded, test_feedback, test_response_data = pre_test_setup()  # passing no tests means test everything
    if check_internet_connection():
        assert test_response_data['totalPointsAwarded'] == test_response_data['totalPointsPossible'], test_feedback
    else:
        output = test_outputs["get_summary_valid_book_and_chapter"]
        assert "Lehi takes his family into the wilderness by the Red Sea—They leave their property" in output

        output = test_outputs["get_summary_invalid_book"]
        assert "Invalid book or chapter" in output

        output = test_outputs["get_summary_invalid_chapter"]
        assert "Invalid book or chapter" in output

        output = test_outputs["program_finishes_without_errors"]
        assert "The program did not finish successfully due to EOFError" not in output

if __name__ == '__main__':
    pytest.main()
