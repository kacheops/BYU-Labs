import pytest
from common_setup import run_test

def test_correct_api_response():
    run_test("correct_api_response","Code properly extracts the data from the JSON object","Make sure your code properly extracts the data from the JSON object")

if __name__ == '__main__':
    pytest.main()