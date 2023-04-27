import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import subprocess
import shlex


# Define the coordinates of the vertices
A = [2, 4]
B = [7, 4]
C = [5.5, 6.5]
D = [5.5, 1.5]

# Define the two lines to be drawn
line1 = [[3.42, 5.23], [3.6, 5]]  
line2 = [[3.42, 2.84], [3.6, 3.12]]  



# Zreate a new plot
fig, ax = plt.subplots()

# Plot the triangle with labels
ax.plot([A[0], B[0]], [A[1], B[1]], 'k', label='AB')
ax.plot([B[0], C[0]], [B[1], C[1]], 'k', label='BC')
ax.plot([A[0], C[0]], [A[1], C[1]], 'k', label='CA')
ax.plot([B[0], D[0]], [B[1], D[1]], 'k', label='BD')
ax.plot([A[0], D[0]], [A[1], D[1]], 'k', label='DA')
plt.plot([line1[0][0], line1[1][0]], [line1[0][1], line1[1][1]], 'r-')
plt.plot([line2[0][0], line2[1][0]], [line2[0][1], line2[1][1]], 'r-')

center = [2,4]
radius = 0.8

start_angle = -35
end_angle = 0

angles = np.linspace(start_angle, end_angle, 100)
x_coords = center[0] + radius * np.cos(np.radians(angles))
y_coords = center[1] + radius * np.sin(np.radians(angles))

#fig, ax = plt.subplots()
ax.plot(x_coords, y_coords, 'k-', linewidth=2)

center = [2,4]
radius = 0.7

start_angle = 0
end_angle = 35

angles = np.linspace(start_angle, end_angle, 100)
x_coords = center[0] + radius * np.cos(np.radians(angles))
y_coords = center[1] + radius * np.sin(np.radians(angles))

#fig, ax = plt.subplots()
ax.plot(x_coords, y_coords, 'k-', linewidth=2)

# Label the vertices
ax.text(A[0], A[1], 'A', ha='center', va='center', fontweight='bold')
ax.text(B[0], B[1], 'B', ha='center', va='center', fontweight='bold')
ax.text(C[0], C[1], 'C', ha='center', va='center', fontweight='bold')
ax.text(D[0], D[1], 'D', ha='center', va='center', fontweight='bold')

# Set the plot limits and title
ax.set_xlim([0, 10])
ax.set_ylim([0, 7.5])
ax.set_title('Quadrilateral ABCD')

# Xdd legend
ax.legend()
#ax.add_patch(angle_plot) 

# Show the plot
plt.savefig('/sdcard/arduino/Vector/figs/graph.png')
subprocess.run(shlex.split("termux-open /sdcard/arduino/Vector/figs/graph.png"))
plt.show()
