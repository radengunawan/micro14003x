import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the Edgeworth box
width = 15  # x-axis for biscuits
height = 10  # y-axis for cola

# Define the utility function
def utility(x, y):
    return x + 2*y

# Create a grid of points for the Edgeworth box
x_values = np.linspace(0, width, 300)
y_values = np.linspace(0, height, 300)
X, Y = np.meshgrid(x_values, y_values)

# Calculate the utility levels for the grid
Z = utility(X, Y)

# Define even integer utility values to plot
even_utility_values = np.arange(2, width + 2*height + 1, 2)

# Plot the Edgeworth box and indifference curves
plt.figure(figsize=(7.5, 5))
plt.contour(X, Y, Z, levels=even_utility_values, colors='blue')
plt.xlim(0, width)
plt.ylim(0, height)
plt.xlabel('Biscuits (x)')
plt.ylabel('Cola (y)')
plt.title('Edgeworth Box with Indifference Curves for Rory')
plt.grid(True)
plt.show()
