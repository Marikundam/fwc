import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import subprocess
import shlex
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#line generation function
def line_gen(A,B):
    len=10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
        temp1 = A + lam_1[i]*(B-A)
        x_AB[:,i] = temp1.T
    return x_AB

A = np.array(([0,0]))
B = np.array(([9,0]))
C = np.array(([8.66,2.5]))
D = np.array(([8.66,-2.5]))

#line generation with the calculated distances(d1,d2,d3)
x_AB = line_gen(A,B)
x_BD = line_gen(B,D)
x_DA = line_gen(D,A)
x_CA = line_gen(C,A)
x_BC = line_gen(B,C)



plt.plot(x_AB[0,:],x_AB[1,:],label='$distance(AB)$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$distance(BC)$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$distance(CA)$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$distance(DA)$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$distance(BD)$')

center = [0.8,0]
radius = 0.8

start_angle = 0
end_angle = 30

angles = np.linspace(start_angle, end_angle, 100)
x_coords = center[0] + radius * np.cos(np.radians(angles))
y_coords = center[1] + radius * np.sin(np.radians(angles))

#fig, ax = plt.subplots()
plt.plot(x_coords, y_coords, 'k-', linewidth=2)

center = [0.8,0]
radius = 0.8

start_angle = 0
end_angle = -30

angles = np.linspace(start_angle, end_angle, 100)
x_coords = center[0] + radius * np.cos(np.radians(angles))
y_coords = center[1] + radius * np.sin(np.radians(angles))

#fig, ax = plt.subplots()
plt.plot(x_coords, y_coords, 'k-', linewidth=2)

sqr_vert = np.vstack((A,B,C,D)).T
plt.scatter(sqr_vert[0,:],sqr_vert[1,:])
vert_labels = ['A','B','C','D']

for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
            (sqr_vert[0,i], sqr_vert[1,i]),
            textcoords = 'offset points',
            xytext = (0,10),
            ha='center')

line1 = [[2.92, 0.72], [2.80, 1.12]]  # First line from X to Y
line2 = [[2.92, -0.72], [2.80, -1.12]]  # Second line from Y to Z
plt.plot([line1[0][0], line1[1][0]], [line1[0][1], line1[1][1]], 'r-')  # First line
plt.plot([line2[0][0], line2[1][0]], [line2[0][1], line2[1][1]], 'g-')  # Second line
plt.xlabel('$x$')                    
plt.ylabel('$y$')
plt.legend(['$AD$','$AC$','$AB$','$BC$','$BD$'])
plt.grid()
plt.axis('equal')
#if using termux
plt.savefig('/sdcard/arduino/Vector/figs/graph.png')
subprocess.run(shlex.split("termux-open /sdcard/arduino/Vector/figs/graph.png"))
plt.title('Quadrilateral ABCD')
plt.show()
