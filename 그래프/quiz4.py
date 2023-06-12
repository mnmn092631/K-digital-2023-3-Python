import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)
gdp = np.array([100, 120, 150, 160, 180, 200, 220, 240, 260, 280, 300])
sales = np.array([50, 70, 30, 45, 60, 80, 70, 90, 110, 100, 120])
prices = np.array([10, 12, 15, 16, 18, 20, 22, 24, 26, 28, 30])

fig = plt.figure()

ax1 = plt.subplot2grid((3, 3), (0, 0), 1, 3)
ax1.plot(years, gdp, marker = 'o', color = 'blue')
ax1.set_title("GDP")
ax1.set_xlabel("Years")
ax1.set_ylabel("GDP (in billions)")

ax2 = plt.subplot2grid((3, 3), (1, 0), 1, 2)
ax2.bar(years, sales, color = 'green')
ax2.set_title("Sales")
ax2.set_xlabel("Years")
ax2.set_ylabel("Quantity Sold")

ax3 = plt.subplot2grid((3, 3), (2, 0), 1, 2)
ax3.plot(years, sales, marker = 'o', color = 'blue')
ax3.set_title("Sales")
ax3.set_xlabel("Years")
ax3.set_ylabel("Quantity Sold")

ax4 = plt.subplot2grid((3, 3), (1, 2), 2, 1)
ax4.scatter(years, prices, color = 'red')
ax4.set_title("Prices")
ax3.set_xlabel("Years")
ax3.set_ylabel("Price")

plt.tight_layout()

plt.show()