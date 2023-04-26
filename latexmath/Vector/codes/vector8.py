import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import subprocess
import shlex
import math
import numpy as np
from numpy import sin, cos, pi, linspace


# Define the coordinates of the vertices
X = [1, 1]
Y = [4, 1]
Z = [3, 4]

P = [5.5,2.5]
Q = [8.5,5.5]
R = [8.5,2]

# Define the two lines to be drawn
line1 = [[2.17, 2.55], [1.98, 2.7]]  # First line from X to Y
line2 = [[2.59, 1.18], [2.59, 0.89]]  # Second line from Y to Z
line3 = [[2.21, 2.65], [2.03, 2.81]] #Third line from X to Y
line7 = [[3.3 ,2.45] , [3.6,2.71]]
line8 = [[3.36 ,2.37] , [3.64,2.64]]
line9 = [[3.42 ,2.29] , [3.68,2.58]]
line4 = [[6.85, 4.14], [7.11, 3.94]]  # First line from P to Q
line5 = [[7.09, 2.35], [7.01, 2.11]]  # Second line from Q to R
line6 = [[7.17, 4], [6.95, 4.2]] #Third line from P to Q
line10 = [[8.36 ,3.73] , [8.66,3.94]]
line11 = [[8.4 ,3.63] , [8.68,3.85]]
line12 = [[8.42 ,3.53] , [8.72,3.77]]


# Zreate a new plot
fig, ax = plt.subplots()

# Plot the triangle with labels
ax.plot([X[0], Y[0]], [X[1], Y[1]], 'k', label='XY')
ax.plot([Y[0], Z[0]], [Y[1], Z[1]], 'k', label='YZ')
ax.plot([Z[0], X[0]], [Z[1], X[1]], 'k', label='ZX')
ax.plot([P[0], Q[0]], [P[1], Q[1]], 'k', label='PQ')
ax.plot([Q[0], R[0]], [Q[1], R[1]], 'k', label='QR')
ax.plot([R[0], P[0]], [R[1], P[1]], 'k', label='RP')
plt.plot([line1[0][0], line1[1][0]], [line1[0][1], line1[1][1]], 'r-')  # First line
plt.plot([line2[0][0], line2[1][0]], [line2[0][1], line2[1][1]], 'g-')  # Second line
plt.plot([line3[0][0], line3[1][0]], [line3[0][1], line3[1][1]], 'r-')
plt.plot([line7[0][0], line7[1][0]], [line7[0][1], line7[1][1]], 'b-')
plt.plot([line8[0][0], line8[1][0]], [line8[0][1], line8[1][1]], 'b-')
plt.plot([line9[0][0], line9[1][0]], [line9[0][1], line9[1][1]], 'b-')
plt.plot([line6[0][0], line6[1][0]], [line6[0][1], line6[1][1]], 'r-')  # First line
plt.plot([line5[0][0], line5[1][0]], [line5[0][1], line5[1][1]], 'g-')  # Second line
plt.plot([line4[0][0], line4[1][0]], [line4[0][1], line4[1][1]], 'r-')
plt.plot([line10[0][0], line10[1][0]], [line10[0][1], line10[1][1]], 'b-')
plt.plot([line11[0][0], line11[1][0]], [line11[0][1], line11[1][1]], 'b-')
plt.plot([line12[0][0], line12[1][0]], [line12[0][1], line12[1][1]], 'b-')


# Label the vertices
ax.text(X[0], X[1], 'X', ha='center', va='center', fontweight='bold')
ax.text(Y[0], Y[1], 'Y', ha='center', va='center', fontweight='bold')
ax.text(Z[0], Z[1], 'Z', ha='center', va='center', fontweight='bold')
ax.text(P[0], P[1], 'P', ha='center', va='center', fontweight='bold')
ax.text(Q[0], Q[1], 'Q', ha='center', va='center', fontweight='bold')
ax.text(R[0], R[1], 'R', ha='center', va='center', fontweight='bold')

# Set the plot limits and title
ax.set_xlim([0, 10])
ax.set_ylim([0, 7.5])
ax.set_title('SSS Criteria')

# Xdd legend
ax.legend()
#ax.add_patch(angle_plot) 

# Show the plot
plt.savefig('/sdcard/arduino/Vector/figs/graph3.png')
subprocess.run(shlex.split("termux-open /sdcard/arduino/Vector/figs/graph3.png"))
plt.show()
