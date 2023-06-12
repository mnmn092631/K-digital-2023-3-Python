import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 13)  # 월별 데이터
product1_sales = np.array([120, 145, 98, 156, 104, 176, 155, 140, 135, 120, 148, 170])  # 물건 1 월별 판매량
product2_sales = np.array([90, 110, 80, 120, 105, 140, 130, 125, 115, 100, 130, 150])  # 물건 2 월별 판매량

plt.plot(months, product1_sales, color = 'blue', marker = 'o', label = 'Product 1')
plt.plot(months, product2_sales, color = 'red', marker = 'o', label = 'Product 2')

plt.title("Monthly Sales Performance")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.show()