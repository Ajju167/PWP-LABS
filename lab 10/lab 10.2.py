import matplotlib.pyplot as plt

# Data for multiple lines
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 3, 4, 5]
y3 = [2, 3, 5, 7, 11]

# Plotting multiple lines
plt.plot(x, y1, label="y = 2x")
plt.plot(x, y2, label="y = x")
plt.plot(x, y3, label="Prime Numbers")

# Add labels and legends
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Multiple Line Plot")
plt.legend()

plt.show()

