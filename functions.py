"""A collection of functions for doing my project."""
from scipy.stats import norm
import math

def hypothesis_testing(null_mean, sample_mean, comparison_symbol, confidence_level, n, sd):
    """
    Perform a hypothesis test to compare a sample mean to a null mean.

    Parameters:
    null_mean (float): The population mean under the null hypothesis.
    sample_mean (float): The sample mean to test.
    comparison_symbol (str): The comparison operator for the alternative hypothesis. 
                             Can be '<', '>', or '!='.
    confidence_level (float): The confidence level for the test (e.g., 0.99 for 99% confidence, 
                               0.95 for 95% confidence, or 0.90 for 90% confidence.).
    n (int): The sample size.
    sd (float): The standard deviation of the sample.

    Returns:
    str: A conclusion based on the hypothesis test.
    """
    
    alpha = 1 - confidence_level
    
    if comparison_symbol not in ['<', '>', '!=']:
        raise ValueError("Invalid comparison symbol. Use '<', '>', or '!='.")
    
    # Calculate the p value
    z_score = (sample_mean - null_mean) / (sd / (n ** 0.5))
    
    # Use the scipy module to calculate z scores 
    if comparison_symbol == "<":
        p_value = norm.cdf(z_score)
    elif comparison_symbol == ">":
        p_value = 1 - norm.cdf(z_score)
    elif comparison_symbol == "!=":
        p_value = 2 * norm.cdf(z_score)
        
    # Return the interpretation of the results
    if p_value > alpha:
        return "Fail to reject the null hypothesis. There is insufficient evidence to conclude that 𝜇 " \
        + str(comparison_symbol) + " " + str(null_mean) + "."
    elif p_value <= alpha:
        return "Reject the null hypothesis. There is sufficient evidence to conclude that 𝜇 " \
        + str(comparison_symbol) + " " + str(null_mean) + "."
    
    # Note: ChatGPT was utilized to create Docstrings, the ValueError, and to use the Scipy Module

    
def percentile(data, percentile):
    """
    Calculate the value at a given percentile for a list of data.

    Parameters:
    data (list of float): The list of data points.
    percentile (float): The desired percentile (a value between 0 and 1).

    Returns:
    float: The value at the specified percentile.
    
    Raises:
    ValueError: If the data list is empty or if percentile is not between 0 and 1.
    """
    
    if not data:
        raise ValueError("Data list is empty.")
    if not 0 <= percentile <= 1:
        raise ValueError("Percentile must be between 0 and 1.")
    
    index = percentile * (len(data)-1)
    ascending_data = sorted(data)
    
    if index == int:
        calc = ascending_data[index]
        
    else:  
        lower_index = math.floor(index)
        upper_index = math.ceil(index)
        
        lower_num = ascending_data[lower_index]
        upper_num = ascending_data[upper_index]
        
        # Interpolation
        calc = lower_num + (upper_num - lower_num) * (index - lower_index)
    
    return calc
    # Note: ChatGPT was utilized to create Docstrings, ValueErrors, and interpolation formula
  
   
def five_num_summary(data):
    """
    Calculate the five-number summary for a list of data.

    The five-number summary includes:
    - Minimum
    - First Quartile (25th percentile)
    - Second Quartile (50th percentile, or median)
    - Third Quartile (75th percentile)
    - Maximum
    - Interquartile Range (IQR)

    Parameters:
    data (list of float): The list of data points.

    Returns:
    dict: A dictionary containing the five-number summary with keys:
          'Minimum', 'First Quartile', 'Second Quartile', 'Third Quartile', 'Maximum', 'Interquartile Range'.
    
    Raises:
    ValueError: If the data list is empty.
    """
    
    if not data:
        raise ValueError("Data list is empty.")
       
    summary = {}
    summary.update({'Minimum' : min(data), 
                    'First Quartile' : percentile(data, .25),
                    'Second Quartile' : percentile(data, .50),
                    'Third Quartile' : percentile(data, .75),
                    'Maximum' : max(data),
                    'Interquartile Range': percentile(data, .75) - percentile(data, .25)
                   })
    return summary
    # Note: ChatGPT was utilized to create Docstrings and ValueErrors
