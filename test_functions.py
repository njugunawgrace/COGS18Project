"""Test for my functions.
"""
import pytest
from scipy.stats import norm
from functions import hypothesis_testing, percentile, five_num_summary

# Note: ChatGPT was utilized to create all Docstrings


# Tests for hypothesis_testing function to check if each operator works as intended
def test_hypothesis_testing_greater_than():
    """
    Test hypothesis_testing for 'greater than' comparison.
    
    Asserts:
    - The result should confirm rejection of the null hypothesis for μ > 50.
    """
    
    result = hypothesis_testing(null_mean=50, sample_mean=55, comparison_symbol='>',
                                confidence_level=0.95, n=30, sd=5)
    expected = "Reject the null hypothesis. There is sufficient evidence to conclude \ 
    that 𝜇 > 50."
    assert result == expected

def test_hypothesis_testing_less_than():
    """
    Test hypothesis_testing for 'less than' comparison.
    
    Asserts:
    - The result should confirm rejection of the null hypothesis for μ < 50.
    """
    
    result = hypothesis_testing(null_mean=50, sample_mean=45, comparison_symbol='<', confidence_level=0.95, n=30, sd=5)
    expected = "Reject the null hypothesis. There is sufficient evidence to conclude \
    that 𝜇 < 50."
    assert result == expected

def test_hypothesis_testing_not_equal():
    """
    Test hypothesis_testing for 'equal to' comparison.
    
    Asserts:
    - The result should confirm rejection of the null hypothesis for μ == 50.
    """
    
    result = hypothesis_testing(null_mean=50, sample_mean=60, comparison_symbol='!=', confidence_level=0.95, n=30, sd=5)
    expected = "Reject the null hypothesis. There is sufficient evidence to conclude \
    that 𝜇 != 50."
    assert result == expected

    
# Tests for percentile function
def test_percentile_empty_data():
    """
    Test percentile function for empty data list.

    Expected behavior:
    - The function should raise a ValueError indicating that the data list is empty.

    Uses:
    - pytest.raises to check for ValueError.

    Raises:
    - ValueError: If the data list is empty.
    """
    
    with pytest.raises(ValueError):
        percentile([], 0.5)

def test_percentile_interpolation():
    """
    Verify the percentile function returns the correct value with interpolation.

    Given a list [10, 20, 30, 40, 50] and the 25th percentile, the function
    should return 20. This tests the function's ability to handle cases where
    interpolation is required.

    Asserts:
    - The calculated 25th percentile value should match the expected value (20).
    """
    
    data = [10, 20, 30, 40, 50]
    result = percentile(data, 0.25)
    expected = 20
    assert result == expected
    
    
# Test the types within the five_num_summary function
def test_five_num_summary():
    """
    Test the five_num_summary function to ensure that the keys are strings, the values are
    floats, and the overall output is a dictionary.
    
    Asserts: 
    - Check the types of the keys, values, and returns.
    """
    assert type(five_num_summary()) == dict
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    summary = five_num_summary(data)
    
    # Check that all keys are strings
    for key in summary.keys():
        assert type(key) == str, f"Key '{key}' is not a string"

    # Check that all values are floats
    for value in summary.values():
        assert type(value) = float, f"Value '{value}' is not a float"
                 
