"""Classes used throughout project"""
#### FINAL PROJECT
#### Stats Tools

import random

class StatisticalAnalysis():
    """
    A class to perform basic statistical analysis on a list of numbers.

    Attributes:
    numlist (list of float): A list of numerical data points.
    """
    
    def __init__(self, numlist):
        """
        Initialize the StatsTools object with a list of numbers.

        Parameters:
        numlist (list of float): A list of numerical data points.
        """
        self.numlist = numlist
        
    
    def mean(self):
        """
        Calculate the mean of the numbers in the list.

        Returns:
        float: The mean of the numbers.
        """
        numsum = 0
        mean = sum(self.numlist) / len(self.numlist)
    
        return mean
        
    
    def mean_diff_sum(self):
        """
        Calculate the sum of squared differences from the mean.

        Returns:
        float: The sum of squared differences from the mean.
        """
        numsum = 0
        mean = self.mean()
        mean_diff_sum = 0
    
        for num in self.numlist:
            numsum = numsum + (num - mean) ** 2
    
        return numsum
        
    
    def stand_dev(self):
        """
        Calculate the standard deviation of the numbers in the list.

        Returns:
        float: The standard deviation of the numbers.
        """
        n = len(self.numlist)
        sd = ((1 / n) * self.mean_diff_sum()) ** 0.5

        return sd


    def confidence_interval(self, n, cl):
        """
        Calculate the confidence interval for the population mean.

        Parameters:
        pop_list (list of float): The population data points.
        n (int): The sample size.
        cl (float): The confidence level (e.g., 0.90, 0.95, 0.99).

        Returns:
        str: A string describing the confidence interval.

        Raises:
        ValueError: If the confidence level is not 0.90, 0.95, or 0.99.
        """
        numlist_tools = StatisticalAnalysis(self.numlist)
        self.n = n
        pop_sd = numlist_tools.stand_dev()
        self.cl = cl
    
        # Convert confidence level to z-score
        if self.cl == 0.99:
            z = 2.81
        elif self.cl == 0.95:
            z = 1.96
        elif self.cl == 0.90:
            z = 1.65
        else:
            raise ValueError("Please pick a Confidence Level: 0.90, 0.95, or 0.99%.")
        
        # Create a random sample of size n from the given population list
        random_sample = random.sample(self.numlist, self.n)
        sample_tools = StatisticalAnalysis(random_sample)
    
        # Calculate the margin of error and interval bounds
        margin_error = z * (numlist_tools.stand_dev() / (self.n ** 0.5))
        lower_bound = sample_tools.mean() - margin_error
        upper_bound = sample_tools.mean() + margin_error
    
        return ("The confidence interval is [" + str(lower_bound) + ", " + str(upper_bound) + "]. " 
              + str(self.cl * 100) + "% of confidence levels computed this way will include the population mean parameter.")  
    
    # Note: ChatGPT was utilized to create Docstrings & to create the ValueError
