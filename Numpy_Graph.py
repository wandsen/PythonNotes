import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0. , 40. , 0.5)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
