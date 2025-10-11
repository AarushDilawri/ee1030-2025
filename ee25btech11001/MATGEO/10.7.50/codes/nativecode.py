import numpy as np
import ctypes
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL('./code.so')
lib.compute_locus.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    ctypes.c_int,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double
]

# Ellipse parameters
A = 4.0
B = 25.0
C = 100.0

# X values
x_vals = np.linspace(-6, 6, 400)
y_vals = np.zeros_like(x_vals)

# Call C function
lib.compute_locus(x_vals, y_vals, len(x_vals), A, B, C)

# Ellipse points
theta = np.linspace(0, 2*np.pi, 400)
ellipse_x = np.sqrt(C/A) * np.cos(theta)
ellipse_y = np.sqrt(C/B) * np.sin(theta)

# Plot
plt.figure(figsize=(8,6))
plt.plot(ellipse_x, ellipse_y, label='Ellipse', color='blue')
plt.plot(x_vals, y_vals, label='Locus (upper branch)', color='red')
plt.plot(x_vals, -y_vals, color='red')  # lower branch symmetric
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.legend()
plt.title("Ellipse and Locus")
plt.show()

