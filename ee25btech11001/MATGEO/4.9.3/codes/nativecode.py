import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

lib = ctypes.CDLL("./code.so")

lib.dot.argtypes = [ctypes.POINTER(ctypes.c_double),
                    ctypes.POINTER(ctypes.c_double),
                    ctypes.c_int]
lib.dot.restype = ctypes.c_double

lib.solve.argtypes = [ctypes.c_double,
                      ctypes.POINTER(ctypes.c_double),
                      ctypes.POINTER(ctypes.c_double),
                      ctypes.c_int,
                      ctypes.POINTER(ctypes.c_double)]
lib.solve.restype = ctypes.c_int

angle = np.pi/3
u_vals = (ctypes.c_double * 3)(2.0, 1.0, 1.0)
p0_vals = (ctypes.c_double * 3)(3.0, 3.0, 0.0)
ts_vals = (ctypes.c_double * 2)()
n = 3

ret = lib.solve(ctypes.c_double(angle), u_vals, p0_vals, ctypes.c_int(n), ts_vals)
if ret != 2:
    raise RuntimeError("solve() failed or returned no real roots")

t1, t2 = ts_vals[0], ts_vals[1]
u = np.array([2.0, 1.0, 1.0])
p0 = np.array([3.0, 3.0, 0.0])
P1 = p0 + t1 * u
P2 = p0 + t2 * u

s = np.linspace(-2, 2, 200)
line1 = np.outer(P1, s)   # shape (3, len(s))
line2 = np.outer(P2, s)

# original line L for context
tL = np.linspace(-2, 2, 200)
L = np.vstack((3 + 2*tL, 3 + 1*tL, 0 + 1*tL))

fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(line1[0], line1[1], line1[2], label='line through origin (P1)', linewidth=2)
ax.plot(line2[0], line2[1], line2[2], label='line through origin (P2)', linewidth=2)
ax.plot(L[0], L[1], L[2], '--', label='given line L', linewidth=1.5)
ax.scatter([0, P1[0], P2[0], 3], [0, P1[1], P2[1], 3], [0, P1[2], P2[2], 0], s=20)
ax.legend()
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
plt.tight_layout()
plt.show()

