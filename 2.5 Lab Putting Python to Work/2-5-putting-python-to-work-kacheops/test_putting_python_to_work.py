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

from tests.common_setup import pre_test_setup, check_internet_connection
import math
import pytest

test_outputs = {}
test_name = None
test_points_awarded = {}
test_response_data = {}

def test_all():
    test_outputs, test_points_awarded, test_feedback, test_response_data = pre_test_setup()  # passing no tests means test everything
    if check_internet_connection():
        assert test_response_data['totalPointsAwarded'] == test_response_data['totalPointsPossible'], test_feedback
    else:
        output = test_outputs["diameter"]

        # Calculate expected diameter
        radius = float(5)
        expected_diameter = 2 * radius

        # Check if the printed output contains the correct diameter value
        assert f"{expected_diameter}" in output.strip(), "The program doesn't calculate the diameter correctly"     

        output = test_outputs["circumference"]
        radius = float(5)
        expected_circumference_314 = 2 * 3.14 * radius
        expected_circumference_math_pi = 2 * math.pi * radius

        # Check if the printed output contains the correct circumference value (either using 3.14 or math.pi)
        assert (f"{expected_circumference_314}" in output.strip() or f"{expected_circumference_math_pi}" in output.strip()),"The program doesn't calculate the circumference correctly"

        output = test_outputs["area"]

        # Calculate expected area for both 3.14 and math.pi
        radius = float(5)
        expected_area_314 = 3.14 * radius**2
        expected_area_math_pi = math.pi * radius**2

        # Check if the printed output contains the correct area value (either using 3.14 or math.pi)
        assert (f"{expected_area_314}" in output.strip() or f"{expected_area_math_pi}" in output.strip()), "The program doesn't calculate the area correctly"        

        output = test_outputs["print_statement"]

        # Convert stdout to lowercase for case-insensitive comparison
        output = output.lower()

        # Check if the final printed message contains information about the diameter, circumference, and area
        assert "diameter" in output.lower().strip(), "The program doesn't mention diameter in the output"
        assert "circumference" in output.lower().strip(), "The program doesn't mention circumference in the output"
        assert "area" in output.lower().strip(), "The program doesn't mention area in the output"

if __name__ == '__main__':
    pytest.main()
