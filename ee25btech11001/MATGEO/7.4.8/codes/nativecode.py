
import ctypes
import numpy as np
import matplotlib.pyplot as plt

# ---- Load the C library --------------------------------------------------
lib = ctypes.CDLL("./code.so")
lib.particle_endpoints.argtypes = [
    ctypes.c_int,
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.double, ndim=1, flags="C_CONTIGUOUS")
]
lib.particle_endpoints.restype = None

# ---- Parameters ---------------------------------------------------------
n = 7
arc_samples = 120
radial_samples = 30

# ---- Get endpoints & angles from C --------------------------------------
px = np.zeros(n, dtype=np.double)
py = np.zeros(n, dtype=np.double)
thetas = np.zeros(n, dtype=np.double)
lib.particle_endpoints(n, px, py, thetas)

# ---- Build continuous trajectory ----------------------------------------
path_x, path_y = [], []
theta_prev = 0.0
r_prev = 1.0
path_x.append(r_prev * np.cos(theta_prev))
path_y.append(r_prev * np.sin(theta_prev))

for k in range(1, n + 1):
    theta_curr = float(thetas[k - 1])
    r_curr = float(k)

    if k == 1:
        # Only arc on C1
        angles = np.linspace(theta_prev, theta_curr, arc_samples + 1)[1:]
        for ang in angles:
            path_x.append(r_curr * np.cos(ang))
            path_y.append(r_curr * np.sin(ang))
    else:
        # Radial outward line
        radii = np.linspace(r_prev, r_curr, radial_samples + 1)[1:]
        for rad in radii:
            path_x.append(rad * np.cos(theta_prev))
            path_y.append(rad * np.sin(theta_prev))

        # Arc motion on C_k
        angles = np.linspace(theta_prev, theta_curr, arc_samples + 1)[1:]
        for ang in angles:
            path_x.append(r_curr * np.cos(ang))
            path_y.append(r_curr * np.sin(ang))

    theta_prev, r_prev = theta_curr, r_curr

# ---- Plotting -----------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_aspect("equal")
ax.set_title("Particle trajectory (up to P₇)")

# Draw circles C₁..C₇
theta_full = np.linspace(0, 2 * np.pi, 400)
for k in range(1, n + 1):
    cx = k * np.cos(theta_full)
    cy = k * np.sin(theta_full)
    ax.plot(cx, cy, linestyle="--", color="gray", linewidth=0.6)

# Plot trajectory
ax.plot(path_x, path_y, color="red", linewidth=1.3, label="trajectory")

# Points P₁..P₇ with coordinates
ax.scatter(px, py, color="blue", zorder=5)
for i in range(n):
    label = f"P{i+1} ({px[i]:.2f},{py[i]:.2f})"
    ax.text(px[i] + 0.15, py[i] + 0.15, label, fontsize=9, color="blue")

# Starting point
ax.scatter([1.0], [0.0], color="black", zorder=6)
ax.text(1.0 + 0.15, 0.0 + 0.15, "Start (1.00,0.00)", fontsize=9, color="black")

# Axes and formatting
ax.axhline(0, color="k", linewidth=0.5)
ax.axvline(0, color="k", linewidth=0.5)
lim = n + 1
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_xlabel("x (cm)")
ax.set_ylabel("y (cm)")
ax.legend()
plt.show()

