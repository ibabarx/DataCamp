"""
Convert monthly_growth_rate, currently a Python list, into a one-dimensional NumPy array called monthly_growth_1D.
Reshape monthly_growth_1D so that it is broadcastable column-wise across monthly_sales; call the new array monthly_growth_2D.
Using broadcasting, multiply each column in monthly_sales by monthly_growth_2D.
"""

# Convert monthly_growth_rate into a NumPy array
monthly_growth_1D = np.array(monthly_growth_rate)

# Reshape monthly_growth_1D
monthly_growth_2D = monthly_growth_1D.reshape((12, 1))

# Multiply each column in monthly_sales by monthly_growth_2D
print(monthly_growth_2D * monthly_sales)
