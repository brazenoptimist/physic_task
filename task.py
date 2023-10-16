import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# Parameters
L = 10
dx = 0.005
dt = 0.005
N = int(L / dx)
c = 1  # Speed in wave equation

x = np.linspace(0, L, N)
v = 1 / 15  # Speed of wave packet
x0 = L / 4  # Initial position of wave packet
u = np.exp(-((x - x0) ** 2)) * np.cos(10 * (x - x0 - v * 0))  # Initial position
u_prev = np.exp(-((x - x0) ** 2)) * np.cos(
    10 * (x - x0 - v * dt)
)  # Initial speed condition

# Plotting
fig, ax = plt.subplots(figsize=(7, 5))
(line,) = ax.plot(x, u, color="C3", lw=2)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
ax.set_title("Wave packet evolution")


def update(num, u, u_prev, line):
    global dx, dt, c
    u_new = np.empty_like(u)

    # Using leapfrog and central difference method for spatial derivative
    for i in range(1, N - 1):
        u_new[i] = (
            2 * u[i]
            - u_prev[i]
            + dt**2 * (u[i + 1] - 2 * u[i] + u[i - 1]) / dx**2
            - dt**2 * np.sin(u[i])
        )

    # Boundary conditions (let's use Dirichlet for simplicity)
    u_new[0] = 0
    u_new[-1] = 0

    u_prev[:] = u[:]
    u[:] = u_new[:]

    line.set_ydata(u)
    return (line,)


ani = anim.FuncAnimation(
    fig, update, frames=2000, fargs=(u, u_prev, line), interval=100, blit=True
)

# gif
ani.save("wave_packet.gif", writer="imagemagick")
plt.show()
