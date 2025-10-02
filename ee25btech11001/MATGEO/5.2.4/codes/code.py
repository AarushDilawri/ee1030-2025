# code.py
import matplotlib.pyplot as plt
import numpy as np

# Example equations: 6x - 3y + 10 = 0, 2x - y + 9 = 0
a1, b1, c1 = 6, -3, 10
a2, b2, c2 = 2, -1, 9

det = a1*b2 - a2*b1
xs = np.linspace(-10, 10, 400)

if det != 0:
    x = (b1*c2 - b2*c1) / det
    y = (c1*a2 - c2*a1) / det
    res = 1
elif (a1*b2 == a2*b1 and a1*c2 == a2*c1 and b1*c2 == b2*c1):
    res = 2
else:
    res = 0

# Plot lines
y1 = -(a1*xs + c1)/b1
y2 = -(a2*xs + c2)/b2
plt.plot(xs, y1, label=f"{a1}x+{b1}y+{c1}=0")
plt.plot(xs, y2, label=f"{a2}x+{b2}y+{c2}=0")

if res == 1:
    plt.scatter([x],[y], color="red", zorder=5, label=f"Unique ({x:.2f},{y:.2f})")
elif res == 2:
    plt.title("Infinite solutions (same line)")
else:
    plt.title("No solution (parallel lines)")

plt.legend()
plt.grid(True)
plt.show()

