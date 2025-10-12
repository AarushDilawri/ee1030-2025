import numpy as np
import matplotlib.pyplot as plt

# Circle parameters
u = np.array([-1.0, -2.0])
f = 1.0
n = np.array([1.0, 0.0])

# Radius and center
r = np.sqrt(np.dot(u, u) - f)
center = -u

# Points of contact
n_norm = n / np.linalg.norm(n)
p1 = center + r * n_norm
p2 = center - r * n_norm

# Circle plotting
theta = np.linspace(0, 2*np.pi, 400)
x = center[0] + r * np.cos(theta)
y = center[1] + r * np.sin(theta)

plt.figure()
plt.plot(x, y, 'b', label='Circle')
plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], color='r', label='Points of contact')

# Tangent lines at x = p1[0], x = p2[0]
y_min, y_max = min(y), max(y)
plt.plot([p1[0], p1[0]], [y_min, y_max], 'g--', label='Tangent')
plt.plot([p2[0], p2[0]], [y_min, y_max], 'g--')

plt.gca().set_aspect('equal')
plt.legend()
plt.grid(True)
plt.title('Circle, Points of Contact & Tangents')
plt.show()

