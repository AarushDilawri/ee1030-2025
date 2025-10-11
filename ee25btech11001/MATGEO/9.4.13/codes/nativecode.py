import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./code.so")

# Define argument and return types
lib.quadratic_roots.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

# Coefficients of x^2 - 4x + 6 = 0
a, b, c = 1.0, -4.0, 6.0

real1 = ctypes.c_double()
imag1 = ctypes.c_double()
real2 = ctypes.c_double()
imag2 = ctypes.c_double()

lib.quadratic_roots(a, b, c, ctypes.byref(real1), ctypes.byref(imag1), ctypes.byref(real2), ctypes.byref(imag2))

# Plot quadratic
x = np.linspace(-2, 6, 400)
y = a*x**2 + b*x + c

plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}')

if imag1.value == 0 and imag2.value == 0:
    plt.scatter([real1.value, real2.value], [0, 0], color='red', label=f'Roots: {real1.value:.2f}, {real2.value:.2f}')
else:
    plt.legend([f'Roots: {real1.value:.2f} ± i{abs(imag1.value):.2f}'])

plt.title('Graphical Solution of Quadratic Equation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

