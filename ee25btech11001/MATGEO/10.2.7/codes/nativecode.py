# nativecode.py
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./code.so")

# Define function signature
lib.find_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double,
                            ctypes.POINTER(ctypes.c_double)]

# Circle parameters (x^2 + y^2 - 2x - 4y + 1 = 0)
u1, u2, f = -1.0, -2.0, 1.0

# Normal vector for line (parallel to y-axis -> x=0)
n1, n2 = 1.0, 0.0

# Prepare output array
out = (ctypes.c_double * 4)()
lib.find_points(u1, u2, f, n1, n2, out)

points = np.array([out[0], out[1], out[2], out[3]]).reshape(2, 2)

# Plotting the circle
theta = np.linspace(0, 2*np.pi, 200)
center = np.array([-u1, -u2])
r = np.sqrt(u1**2 + u2**2 - f)
x = center[0] + r*np.cos(theta)
y = center[1] + r*np.sin(theta)

plt.figure()
plt.plot(x, y, 'b', label='Circle')
plt.scatter(points[:, 0], points[:, 1], color='r', label='Points of contact')
plt.gca().set_aspect('equal')
plt.legend()
plt.grid(True)
plt.title('Circle and Points of Contact')
plt.show()

