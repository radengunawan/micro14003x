# Fay's utility function: min(x, y)
def fay_utility(x, y):
    return np.minimum(x, y)

# Create a new set of grid points, but note that Fay's origin is in the top-right corner
X_fay = np.linspace(0, width, 300)
Y_fay = np.linspace(0, height, 300)
X_fay, Y_fay = np.meshgrid(X_fay, Y_fay)

# Since Fay's origin is in the top-right corner, we need to reflect the grid accordingly
X_fay_reflected = width - X_fay
Y_fay_reflected = height - Y_fay

# Calculate the utility levels for Fay's grid
Z_fay = fay_utility(X_fay_reflected, Y_fay_reflected)

# Define integer utility values for Fay to plot
utility_values_fay = np.arange(1, 11, 1)

# Plot the Edgeworth box and indifference curves for Rory
plt.figure(figsize=(8, 5))
plt.contour(X, Y, Z, levels=even_utility_values, colors='blue', label="Rory's Indifference Curves")

# Plot Fay's indifference curves on the same Edgeworth box
plt.contour(X_fay, Y_fay, Z_fay, levels=utility_values_fay, colors='red', linestyles='--', label="Fay's Indifference Curves")

plt.xlim(0, width)
plt.ylim(0, height)
plt.xlabel('Biscuits (x)')
plt.ylabel('Cola (y)')
plt.title('Edgeworth Box with Indifference Curves for Rory and Fay')
plt.grid(True)

# Add a legend to distinguish between the two sets of curves
plt.legend(["Rory's Indifference Curves", "Fay's Indifference Curves"])
plt.show()
