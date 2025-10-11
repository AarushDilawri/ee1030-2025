import numpy as np
import matplotlib.pyplot as plt

# ---- Parameters ---------------------------------------------------------
n = 7
arc_samples = 120
radial_samples = 30

# ---- Compute endpoints and angles ---------------------------------------
px, py, thetas = np.zeros(n), np.zeros(n), np.zeros(n)
theta = 0.0
for k in range(1, n + 1):
    theta += 1.0  # 1 rad per circle
    px[k - 1] = k * np.cos(theta)
    py[k - 1] = k * np.sin(theta)
    thetas[k - 1] = theta

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
        # Arc on C1
        angles = np.linspace(theta_prev, theta_curr, arc_samples + 1)[1:]
        for ang in angles:
            path_x.append(r_curr * np.cos(ang))
            path_y.append(r_curr * np.sin(ang))
    else:
        # Radial outward
        radii = np.linspace(r_prev, r_curr, radial_samples + 1)[1:]
        for rad in radii:
            path_x.append(rad * np.cos(theta_prev))
            path_y.append(rad * np.sin(theta_prev))

        # Arc on C_k
        angles = np.linspace(theta_prev, theta_curr, arc_samples + 1)[1:]
        for ang in angles:
            path_x.append(r_curr * np.cos(ang))
            path_y.append(r_curr * np.sin(ang))

    theta_prev, r_prev = theta_curr, r_curr

# ---- Plotting -----------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_aspect("equal")
ax.set_title("Particle trajectory (pure Python)")

# Circles
theta_full = np.linspace(0, 2 * np.pi, 400)
for k in range(1, n + 1):
    ax.plot(k * np.cos(theta_full), k * np.sin(theta_full),
            linestyle="--", color="gray", linewidth=0.6)

# Trajectory
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

