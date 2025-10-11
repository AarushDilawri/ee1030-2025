import numpy as np
import matplotlib.pyplot as plt

# Given parameters
x0, y0 = -3.0, 1.0
e = np.sqrt(2.0/5.0)

# Step 1: V matrix before scaling
V11 = 1 - e**2
V22 = 1

# Step 2: Scale to satisfy (x0,y0)
val = V11*x0**2 + V22*y0**2
scale = 1.0 / val
A = V11 * scale
B = V22 * scale
C = 1.0

print(f"Ellipse equation (Python): {A:.6f} x^2 + {B:.6f} y^2 = {C:.6f}")

# Step 3: Plot
theta = np.linspace(0, 2*np.pi, 400)
a = np.sqrt(C/A)
b = np.sqrt(C/B)
x = a * np.cos(theta)
y = b * np.sin(theta)

plt.figure(figsize=(6,6))
plt.plot(x, y, label=f"{A:.2f} x² + {B:.2f} y² = {C:.0f}")
plt.scatter(x0, y0, color='red', label='(-3,1)')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.title('Ellipse (Python only)')
plt.show()

