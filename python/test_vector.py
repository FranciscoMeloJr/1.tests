import matplotlib.pyplot as plt
import numpy as np
 
pi = np.pi
print(pi)

#X, Y = np.mgrid[-pi:pi:10j, -pi:pi:10j]
X = [[2 -3.14159265][2 -2]]
Y = [[-3.14159265 -2][2 -2]]

print(X)
print(Y)

U = np.sin(X)
V = np.cos(Y)
 
plt.figure()
plt.quiver(X, Y, U, V)
plt.show()
