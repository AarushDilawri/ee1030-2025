import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL('./code.so')

# Define argument and return types
lib.ellipse_equation.argtypes = [ctypes.POINTER(ctypes.c_double),
                                 ctypes.POINTER(ctypes.c_double),
                                 ctypes.POINTER(ctypes.c_double),
                                 ctypes.c_double,
                                 ctypes.c_double,
                                 ctypes.c_double]
lib.ellipse_equation.restype = ctypes.c_int  # returning int now

# Prepare variables
A = ctypes.c_double()
B = ctypes.c_double()
C = ctypes.c_double()
x0 = -3.0
y0 = 1.0
e = np.sqrt(2.0/5.0)

# Call the C function
ret = lib.ellipse_equation(ctypes.byref(A), ctypes.byref(B), ctypes.byref(C), x0, y0, e)

if ret != 0:
    raise RuntimeError("Error computing ellipse coefficients in C.")

print(f"Ellipse equation from C: {A.value:.6f} x^2 + {B.value:.6f} y^2 = {C.value:.6f}")

# Plot the ellipse
theta = np.linspace(0, 2*np.pi, 400)
a = np.sqrt(C.value/A.value)
b = np.sqrt(C.value/B.value)
x = a * np.cos(theta)
y = b * np.sin(theta)

plt.figure(figsize=(6,6))
plt.plot(x, y, label=f"{A.value:.2f} x² + {B.value:.2f} y² = {C.value:.0f}")
plt.scatter(x0, y0, color='red', label='(-3,1)')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.title('Ellipse from C Library')
plt.show()

