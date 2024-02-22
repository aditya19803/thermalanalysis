import numpy as np
import matplotlib.pyplot as plt

Lx = float(input('Enter plate length: ') )
Ly = float(input('Enter plate width: ') )
nx = int(input('Enter number of nodes in the x-direction: '))
ny = int(input('Enter number of nodes in the y-direction: '))
dx = Lx / (nx - 1)  # node spacing in the x-direction
dy = Ly / (ny - 1)  # node spacing in the y-direction

# thermal properties of the plate
k = float(input('Enter thermal conductivity: '))
rho = float(input('Enter density: '))
c = float(input('Enter specific heat: '))

Q = float(input('Enter heat source intensity: '))  # heat source

# simulation parameters
nt = int(input('Enter number of time steps: '))
dt = float(input('Enter time step size: '))

# temperature field
T = np.zeros((nx, ny))

# Time-stepping loop
for n in range(nt):
    Tn = T.copy()
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            T[i, j] = Tn[i, j] + k * dt / (rho * c) * (
                (Tn[i + 1, j] - 2 * Tn[i, j] + Tn[i - 1, j]) / dx ** 2 +
                (Tn[i, j + 1] - 2 * Tn[i, j] + Tn[i, j - 1]) / dy ** 2
            )
    T[:, 0] = 100  # left boundary condition
    T[:, -1] = 50  # right boundary condition
    T[0, :] = 0  # top boundary condition
    T[-1, :] = 50  # bottom boundary condition
    T[nx//2, ny//2] += Q*dt #add heat source

# Plot of temperature field
plt.imshow(T, cmap='hot', extent=[0, Lx, 0, Ly])
plt.colorbar().set_label('Temperature (C)')
plt.title('2D Heat Transfer Simulation')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()
