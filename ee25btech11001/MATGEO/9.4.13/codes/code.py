import numpy as np
import matplotlib.pyplot as plt
import cmath

# Coefficients
a, b, c = 1, -4, 6

# Discriminant
D = b**2 - 4*a*c

root1 = (-b + cmath.sqrt(D)) / (2*a)
root2 = (-b - cmath.sqrt(D)) / (2*a)

# Plot quadratic
x = np.linspace(-2, 6, 400)
y = a*x**2 + b*x + c

plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}')

if root1.imag == 0 and root2.imag == 0:
    plt.scatter([root1.real, root2.real], [0, 0], color='red', label=f'Roots: {root1.real:.2f}, {root2.real:.2f}')
else:
    plt.legend([f'Roots: {root1.real:.2f} ± i{abs(root1.imag):.2f}'])

plt.title('Graphical Solution of Quadratic Equation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

