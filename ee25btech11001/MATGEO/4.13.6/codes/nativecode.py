import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./code.so")

# Define function signature
lib.locus_value.argtypes = [
    ctypes.c_int,                           # dimension
    np.ctypeslib.ndpointer(dtype=np.double), # A
    np.ctypeslib.ndpointer(dtype=np.double), # B
    np.ctypeslib.ndpointer(dtype=np.double), # P
    ctypes.c_double                         # D
]
lib.locus_value.restype = ctypes.c_double

# Example: A=(0,4), B=(0,-4), delta=6
A = np.array([0.0, 4.0], dtype=np.double)
B = np.array([0.0, -4.0], dtype=np.double)
D = 6.0

# Create grid and evaluate locus
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        P = np.array([X[i,j], Y[i,j]], dtype=np.double)
        Z[i,j] = lib.locus_value(2, A, B, P, D)

# Plot contour Z=0 (the locus)
# Plot the locus
plt.contour(X, Y, Z, levels=[0], colors="red")

# Plot the foci points A and B
plt.scatter(A[0], A[1], color="blue", label="A (focus)")
plt.scatter(B[0], B[1], color="green", label="B (focus)")

# Coordinate axes
plt.axhline(0, color="k", linewidth=0.5)
plt.axvline(0, color="k", linewidth=0.5)

# Make the plot pretty
plt.gca().set_aspect("equal")
plt.legend()
plt.title("Locus of P such that |AP − BP| = 6")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

