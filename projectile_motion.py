import numpy as np
import matplotlib.pyplot as plt

g = 9.8
a = 4.9
u = 20
theta = 45

r_theta = np.radians(theta)

ux = u * np.cos(r_theta)
uy = u * np.sin(r_theta)

t_f = (2 * uy) / g
t = np.linspace(0, t_f, 100)

x = ux * t
y = (uy * t) - (a * (t**2))

fig, ax = plt.subplots()
ax.plot(x,y)
max_index = np.argmax(y)
ymax = y[max_index]
x_at_ymax = x[max_index]
ax.plot(x_at_ymax, ymax, marker="o", ms="10")
ax.annotate(
    f"Highest point\n({x_at_ymax:.2f},{ymax:.2f})",
    xy = (x_at_ymax, ymax),
    xytext = (x_at_ymax + 2, ymax - 2),
    arrowprops=dict(
        arrowstyle="->",
        color = "black",
        lw = 1.5
    ),
    fontsize = 11,
    fontweight = "bold"
)
ax.set_title("PROJECTILE MOTION MAPPED")
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Distance (m)")
ax.grid(True)
plt.show()
