"""
Extract 'realinc' from gss and compute its logarithm using np.log10().
Compute the mean and standard deviation of the result.
Make a norm object by passing the computed mean and standard deviation to norm().
"""

# Extract realinc and compute its log
income = gss['realinc']
log_income = np.log10(income)

# Compute mean and standard deviation
mean = log_income.mean()
std = log_income.std()
print(mean, std)

# Make a norm object
from scipy.stats import norm
dist = norm(mean,std)
