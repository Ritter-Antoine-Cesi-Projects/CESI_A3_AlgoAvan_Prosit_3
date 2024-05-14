import numpy as np
import matplotlib.pyplot as plt

xmax = 10
ymax = 10
plt.plot(xmax, ymax)

# On trace la droite x + y <= 100
x1 = np.linspace(0, xmax, ymax)
y1 = xmax - x1
plt.plot(x1, y1)
plt.fill_between(x1, y1, ymax, color='gray', alpha=0.5)

# On trace la droite pour que x ne soit jamais plus grand que 50% de x + y
x2 = np.linspace(0, xmax, ymax)
y2 = x2
plt.plot(x2, y2)
plt.fill_between(x2, y2, color='gray', alpha=0.5)

# On trace la droite pour que y ne soit jamais plus grand que 80% de x + y
x3 = np.linspace(0, xmax, ymax)
y3 = 4 * x3
plt.plot(x3, y3)
plt.fill_between(x3, y3, ymax, color='gray', alpha=0.5)

# Trouver l'ensemble des points qui respectent les contraintes et les afficher
for x in range(xmax):
    for y in range(ymax):
        if x + y <= xmax and 0.5 * x - 0.5 * y <= 0 and -0.8 * x + 0.2 * y <= 0:
            plt.plot(x, y, 'bo', alpha=0.5)

plt.xlim(0, xmax)
plt.ylim(0, ymax)
plt.show()