import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
x_values = np.linspace(0, 10, 100)
y1_values = np.sin(x_values)
y2_values = np.cos(x_values)

# Plot the curves
plt.plot(x_values, y1_values, label='sin(x)')
plt.plot(x_values, y2_values, label='cos(x)')

# Fill the area between the curves
plt.fill_between(x_values, y1_values, y2_values, color='gray', alpha=0.3, label='Fill Between sin(x) and cos(x)')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Fill Between sin(x) and cos(x)')
plt.legend()

# Show the plot
plt.show()