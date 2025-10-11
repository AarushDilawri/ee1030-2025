import numpy as np
import matplotlib.pyplot as plt

# Ellipse parameters
A = 4.0
B = 25.0
C = 100.0

# Function to compute locus y for each x
def compute_locus_py(x_vals, A, B):
    y_vals = np.zeros_like(x_vals)
    for i, x in enumerate(x_vals):
        denom = A * x**2 - B
        if denom == 0:
            y_vals[i] = np.nan
            continue
        y2 = (A * x**2) / denom
        if y2 < 0:
            y_vals[i] = np.nan
            continue
        y_vals[i] = np.sqrt(y2)
    return y_vals

# X values
x_vals = np.linspace(-6, 6, 400)
y_vals = compute_locus_py(x_vals, A, B)

# Ellipse points
theta = np.linspace(0, 2*np.pi, 400)
ellipse_x = np.sqrt(C/A) * np.cos(theta)
ellipse_y = np.sqrt(C/B) * np.sin(theta)

# Plot
plt.figure(figsize=(8,6))
plt.plot(ellipse_x, ellipse_y, label='Ellipse', color='blue')
plt.plot(x_vals, y_vals, label='Locus (upper branch)', color='red')
plt.plot(x_vals, -y_vals, color='red')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.legend()
plt.title("Ellipse and Locus")
plt.show()

