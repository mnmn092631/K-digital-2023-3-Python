import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = plt.subplot2grid((3, 3), (0, 0), 1, 3)
ax1.plot([1, 2, 3, 4], [1, 4, 2, 3])

ax2 = plt.subplot2grid((3, 3), (1, 0), 1,2)
ax2.plot([1, 2, 3, 4], [1, 4, 2, 3])

ax3 = plt.subplot2grid((3, 3), (1, 2), 2, 1)
ax3.plot([1, 2, 3, 4], [1, 4, 2, 3])

ax4 = plt.subplot2grid((3, 3), (2, 0), 1, 2)
ax4.plot([1, 2, 3, 4], [1, 4, 2, 3])

plt.tight_layout()

plt.show()
