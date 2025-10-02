# nativecode.py
import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load shared library
lib = ctypes.CDLL("./code.so")

lib.solve_linear.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                             ctypes.c_double, ctypes.c_double, ctypes.c_double,
                             ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.solve_linear.restype = ctypes.c_int

# Example equations: 6x - 3y + 10 = 0, 2x - y + 9 = 0
a1, b1, c1 = 6, -3, 10
a2, b2, c2 = 2, -1, 9

x = ctypes.c_double()
y = ctypes.c_double()

res = lib.solve_linear(a1,b1,c1,a2,b2,c2,ctypes.byref(x),ctypes.byref(y))

# Plot
xs = np.linspace(-10, 10, 400)
y1 = -(a1*xs + c1)/b1
y2 = -(a2*xs + c2)/b2

plt.plot(xs, y1, label=f"{a1}x+{b1}y+{c1}=0")
plt.plot(xs, y2, label=f"{a2}x+{b2}y+{c2}=0")

if res == 1:
    plt.scatter([x.value],[y.value], color="red", zorder=5,
                label=f"Unique ({x.value:.2f},{y.value:.2f})")
elif res == 2:
    plt.title("Infinite solutions (same line)")
else:
    plt.title("No solution (parallel lines)")

plt.legend()
plt.grid(True)
plt.show()

