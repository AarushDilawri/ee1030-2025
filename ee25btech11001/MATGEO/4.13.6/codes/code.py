import numpy as np
import matplotlib.pyplot as plt

def inner_product(u, v):
    return np.dot(u, v)

def locus_value(A, B, P, D):
    u = A - B
    alpha = inner_product(A, A) - inner_product(B, B)

    # Quadratic part
    quad = (np.dot(P, u))**2 - D*D*inner_product(P, P)

    # Linear part
    coeff = -(D*D+alpha)*u + 2*D*D*A
    lin = inner_product(coeff, P)

    # Constant part
    constant = ((D*D+alpha)**2)/4.0 - D*D*inner_product(A, A)

    return quad + lin + constant

# Example: A=(0,4), B=(0,-4), delta=6
A = np.array([0.0, 4.0])
B = np.array([0.0, -4.0])
D = 6.0

x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        P = np.array([X[i,j], Y[i,j]])
        Z[i,j] = locus_value(A, B, P, D)

plt.contour(X, Y, Z, levels=[0], colors="red")
plt.axhline(0, color="k", linewidth=0.5)
plt.axvline(0, color="k", linewidth=0.5)
plt.gca().set_aspect("equal")
plt.title("Locus")
plt.show()
