
import pytest
from common_setup import run_test

def test_program_finish():
    run_test("program_finish", "Your \"tilling the soil program\" still works after authorization", "The program did not finish successfully.")

if __name__ == '__main__':
    pytest.main()