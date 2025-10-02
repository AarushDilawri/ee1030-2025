import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

u = np.array([2.0, 1.0, 1.0])
p0 = np.array([3.0, 3.0, 0.0])
angle = np.pi/3
c2 = np.cos(angle)**2

U = u @ u
W = u @ p0
Q = p0 @ p0

one_minus_c2 = 1.0 - c2
A = one_minus_c2 * U * U
B = 2.0 * one_minus_c2 * U * W
C = W * W - c2 * U * Q

roots = np.roots([A, B, C])
t1, t2 = roots[0], roots[1]
P1 = p0 + t1 * u
P2 = p0 + t2 * u

s = np.linspace(-2, 2, 200)
line1 = np.outer(P1, s)
line2 = np.outer(P2, s)

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

