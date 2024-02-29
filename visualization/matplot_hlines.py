import matplotlib.pyplot as plt

# Create some sample data
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

# Plot the data
plt.plot(x_values, y_values, label='Data')

# Draw a horizontal line at y=5
plt.hlines(y=5, xmin=min(x_values), xmax=max(x_values), colors='red', linestyles='dashed', label='Horizontal Line at y=5')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot with Horizontal Line')
plt.legend()

# Show the plot
plt.show()
