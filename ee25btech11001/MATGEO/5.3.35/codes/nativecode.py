import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
code = ctypes.CDLL("./code.so")

# Declare function signature
code.find_r.restype = ctypes.c_double
code.find_r.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]

# Given coefficients
a1, b1, c1 = 3, -1, 8
a2, c2 = 6, 16

# Call C function
r = code.find_r(a1, b1, c1, a2, c2)
print("Value of r:", r)

# Define line equations
def line1(x): return (a1*x + c1)/(-b1)
def line2(x): return (a2*x + c2)/(-(-r))

# Plot
x = np.linspace(-10, 10, 100)
plt.plot(x, line1(x), label="Line 1")
plt.plot(x, line2(x), label="Line 2 (with r)")
plt.legend()
plt.grid(True)
plt.show()

