import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
mp.use("TkAgg")

A=np.array([[1,1],[1,-1]],dtype=float)
b=np.array([5,1], dtype=float)

x=np.linalg.solve(A,b)
print("Solution vector for the system of equations:",x)

# Making a plot
x_vals = np.linspace(-2, 10, 400)

# Rearranged equations to express y in terms of x
y1 = (5 - x_vals)        # from x + 3y = 6
y2 = (x_vals-1)    # from 2x - 3y = 12

# Plot lines
plt.plot(x_vals, y1, label=r"$x + y = 5$")
plt.plot(x_vals, y2, label=r"$x - y = 1$")

# Mark solution
plt.scatter(x[0], x[1], color="red", zorder=5)
plt.text(x[0]+0.2, x[1], f"({x[0]:.1f}, {x[1]:.1f})", color="red")

# Formatting
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphical Solution of the Linear System")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.grid(True)
plt.savefig("Figure_2")
plt.show()
