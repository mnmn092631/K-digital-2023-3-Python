import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.plot(x, y)

plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('y')

plt.show()