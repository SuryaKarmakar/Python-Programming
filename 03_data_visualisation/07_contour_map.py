import numpy as np
import matplotlib.pyplot as plt

# Create sample data (2D grid)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)


# Define a function to calculate the data values (z-values)
def calculateZ(x, y):
    return np.sin(np.sqrt(x**2 + y**2))


Z = calculateZ(X, Y)

# Create a contour plot
contours = plt.contour(X, Y, Z, colors="black")

# Label the contour lines with their values
plt.clabel(contours, inline=True, fontsize=8)

# Add a colorbar for reference
plt.colorbar()

# Add labels and a title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Contour Map Example")

# Show the plot
plt.show()
