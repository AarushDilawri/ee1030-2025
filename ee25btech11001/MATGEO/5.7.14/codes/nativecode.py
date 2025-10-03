import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
code = ctypes.CDLL("./code.so")

# Define argument and return types
code.char_poly.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                           np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C")]

# Coefficients array
coeffs = np.zeros(3, dtype=np.float64)

# Given matrix A
a11, a12, a21, a22 = -3, 6, -2, 4

# Call C function
code.char_poly(a11, a12, a21, a22, coeffs)
print("Characteristic Polynomial Coefficients:", coeffs)

# Define polynomial
lam = np.linspace(-10, 10, 400)
poly_vals = coeffs[0]*lam**2 + coeffs[1]*lam + coeffs[2]

# Plot
plt.axhline(0, color='black', linewidth=0.8)
plt.plot(lam, poly_vals, label="Characteristic Polynomial")
plt.xlabel("λ")
plt.ylabel("p(λ)")
plt.legend()
plt.grid(True)
plt.show()

