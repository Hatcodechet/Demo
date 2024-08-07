import numpy as np
import matplotlib.pyplot as plt

# Data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 8])

# Fitted line
a0 = 0.8
a1 = 1.4
y_fit = a0 + a1 * x

# Plot
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, y_fit, color='red', label='Fitted line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
