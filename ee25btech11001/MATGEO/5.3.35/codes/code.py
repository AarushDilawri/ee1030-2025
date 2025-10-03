import numpy as np
import matplotlib.pyplot as plt

# Coefficients from the problem
a1, b1, c1 = 3, -1, 8
a2, b2, c2 = 6, -2, 16   # since r = 2

# Define line equations
def line1(x): return (a1*x + c1)/(-b1)
def line2(x): return (a2*x + c2)/(-b2)

# Plot
x = np.linspace(-10, 10, 100)
plt.plot(x, line1(x), label="Line 1")
plt.plot(x, line2(x), label="Line 2 (r=2)")
plt.legend()
plt.grid(True)
plt.show()

