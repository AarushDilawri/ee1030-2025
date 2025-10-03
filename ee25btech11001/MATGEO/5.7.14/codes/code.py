import numpy as np
import matplotlib.pyplot as plt

# Given matrix A
a11, a12, a21, a22 = -3, 6, -2, 4

# Compute trace and determinant
trace = a11 + a22
det = a11*a22 - a12*a21

# Polynomial coefficients
coeffs = [1, -trace, det]
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

