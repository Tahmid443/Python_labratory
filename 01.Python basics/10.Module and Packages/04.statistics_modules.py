"""
================================================================================
STATISTICS MODULE - COMPLETE METHOD REFERENCE
================================================================================

All methods are imported from Python's built-in statistics module.

================================================================================
METHOD SUMMARY TABLE
================================================================================

Method                          Description
------------------------------- -------------------------------------------------
statistics.harmonic_mean()      Calculates the harmonic mean (central location) of the given data
statistics.mean()               Calculates the mean (average) of the given data
statistics.median()             Calculates the median (middle value) of the given data
statistics.median_grouped()     Calculates the median of grouped continuous data
statistics.median_high()        Calculates the high median of the given data
statistics.median_low()         Calculates the low median of the given data
statistics.mode()               Calculates the mode (central tendency) of the given numeric or nominal data
statistics.pstdev()             Calculates the standard deviation from an entire population
statistics.stdev()              Calculates the standard deviation from a sample of data
statistics.pvariance()          Calculates the variance of an entire population
statistics.variance()           Calculates the variance from a sample of data

================================================================================
IMPORT STATEMENT
================================================================================
"""

import statistics
from statistics import (
    harmonic_mean,
    mean,
    median,
    median_grouped,
    median_high,
    median_low,
    mode,
    pstdev,
    stdev,
    pvariance,
    variance,
)

"""
================================================================================
1. HARMONIC_MEAN - Harmonic mean (central location)
================================================================================
"""

# harmonic_mean(data, weights=None) - Calculates harmonic mean
data = [40, 60, 80]
statistics.harmonic_mean(data)
# Returns: 54.54545454545454

# With weights
statistics.harmonic_mean(data, weights=[1, 2, 3])
# Returns weighted harmonic mean

# Used for rates, speeds, and ratios

"""
================================================================================
2. MEAN - Arithmetic mean (average)
================================================================================
"""

# mean(data) - Calculates the arithmetic mean
data = [10, 20, 30, 40, 50]
statistics.mean(data)
# Returns: 30.0

# Works with integers and floats
statistics.mean([1, 2, 3, 4, 5])
# Returns: 3.0

# Raises StatisticsError if data is empty
# statistics.mean([])  # StatisticsError

"""
================================================================================
3. MEDIAN - Middle value
================================================================================
"""

# median(data) - Calculates median (middle value)
data = [1, 3, 5, 7, 9]  # Odd number of elements
statistics.median(data)
# Returns: 5

data = [1, 3, 5, 7]  # Even number of elements
statistics.median(data)
# Returns: 4.0 (average of 3 and 5)

"""
================================================================================
4. MEDIAN_GROUPED - Median of grouped continuous data
================================================================================
"""

# median_grouped(data, interval=1) - Median for grouped continuous data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
statistics.median_grouped(data)
# Returns: 5.0

# With interval parameter
statistics.median_grouped(data, interval=2)
# Returns median with specified class interval

# Used for continuous data grouped into intervals

"""
================================================================================
5. MEDIAN_HIGH - High median
================================================================================
"""

# median_high(data) - Returns the high median
data = [1, 3, 5, 7, 9]  # Odd number of elements
statistics.median_high(data)
# Returns: 5 (same as median for odd count)

data = [1, 3, 5, 7]  # Even number of elements
statistics.median_high(data)
# Returns: 5 (higher of the two middle values: 5)

"""
================================================================================
6. MEDIAN_LOW - Low median
================================================================================
"""

# median_low(data) - Returns the low median
data = [1, 3, 5, 7, 9]  # Odd number of elements
statistics.median_low(data)
# Returns: 5 (same as median for odd count)

data = [1, 3, 5, 7]  # Even number of elements
statistics.median_low(data)
# Returns: 3 (lower of the two middle values: 3)

"""
================================================================================
7. MODE - Most frequent value (central tendency)
================================================================================
"""

# mode(data) - Calculates the mode (most frequent value)
data = [1, 2, 2, 3, 4, 4, 4, 5]
statistics.mode(data)
# Returns: 4 (appears 3 times)

# Works with nominal data (strings)
data = ["red", "blue", "red", "green", "red"]
statistics.mode(data)
# Returns: 'red'

# Raises StatisticsError if no unique mode exists
# statistics.mode([1, 1, 2, 2])  # StatisticsError: no unique mode

"""
================================================================================
8. PSTDEV - Population standard deviation
================================================================================
"""

# pstdev(data, mu=None) - Standard deviation of an entire population
population = [1, 2, 3, 4, 5]
statistics.pstdev(population)
# Returns: 1.4142135623730951

# With known population mean
statistics.pstdev(population, mu=3.0)
# Returns standard deviation with known mean

# Used when data represents the entire population

"""
================================================================================
9. STDEV - Sample standard deviation
================================================================================
"""

# stdev(data, xbar=None) - Standard deviation from a sample
sample = [1, 2, 3, 4, 5]
statistics.stdev(sample)
# Returns: 1.5811388300841898

# With known sample mean
statistics.stdev(sample, xbar=3.0)
# Returns standard deviation with known mean

# Used when data is a sample from a larger population

"""
================================================================================
10. PVARIANCE - Population variance
================================================================================
"""

# pvariance(data, mu=None) - Variance of an entire population
population = [1, 2, 3, 4, 5]
statistics.pvariance(population)
# Returns: 2.0

# With known population mean
statistics.pvariance(population, mu=3.0)
# Returns variance with known mean

# Used when data represents the entire population

"""
================================================================================
11. VARIANCE - Sample variance
================================================================================
"""

# variance(data, xbar=None) - Variance from a sample
sample = [1, 2, 3, 4, 5]
statistics.variance(sample)
# Returns: 2.5

# With known sample mean
statistics.variance(sample, xbar=3.0)
# Returns variance with known mean

# Used when data is a sample from a larger population

"""
================================================================================
QUICK COMPARISON - POPULATION VS SAMPLE
================================================================================

                        POPULATION (Full data)    SAMPLE (Subset of data)
Standard Deviation      pstdev()                  stdev()
Variance                pvariance()               variance()

Population functions divide by N (number of data points)
Sample functions divide by N-1 (Bessel's correction)
"""

"""
================================================================================
COMPLETE REFERENCE SUMMARY
================================================================================

Method Name          Parameter        Returns              Use Case
------------------   ---------------  ------------------  -----------------------
harmonic_mean()      data, weights    float               Rates/ratios
mean()               data             float               Average
median()             data             float/int           Middle value
median_grouped()     data, interval   float               Grouped continuous data
median_high()        data             float/int           Higher median
median_low()         data             float/int           Lower median
mode()               data             value               Most frequent value
pstdev()             data, mu         float               Population std dev
stdev()              data, xbar       float               Sample std dev
pvariance()          data, mu         float               Population variance
variance()           data, xbar       float               Sample variance

================================================================================
ERRORS TO BE AWARE OF
================================================================================

StatisticsError - Raised when:
    - Empty data passed to mean, median, pstdev, etc.
    - No unique mode found in mode()
    - Less than two data points for variance/stdev
"""

"""
================================================================================
FULL EXAMPLE - ALL METHODS IN ONE FILE
================================================================================
"""

import statistics

# Sample dataset
data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Central tendency
statistics.harmonic_mean(data)  # Harmonic mean
statistics.mean(data)  # Arithmetic mean
statistics.median(data)  # Median
statistics.median_grouped(data)  # Grouped median
statistics.median_high(data)  # High median
statistics.median_low(data)  # Low median
statistics.mode(data)  # Mode (if unique)

# Dispersion
statistics.pstdev(data)  # Population standard deviation
statistics.stdev(data)  # Sample standard deviation
statistics.pvariance(data)  # Population variance
statistics.variance(data)  # Sample variance
