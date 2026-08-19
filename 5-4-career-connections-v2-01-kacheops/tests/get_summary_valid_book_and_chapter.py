import pytest
from common_setup import pre_test_setup, check_internet_connection

def test_get_summary_valid_book_and_chapter():
    test_outputs, test_points_awarded, test_feedback, test_response_data = pre_test_setup("get_summary_valid_book_and_chapter")
    if check_internet_connection():
        assert test_response_data['totalPointsAwarded'] == test_response_data['totalPointsPossible'], test_feedback
    else:
        output = test_outputs["get_summary_valid_book_and_chapter"]
        assert "Lehi takes his family into the wilderness by the Red Sea—They leave their property" in output

if __name__ == '__main__':
    pytest.main()
