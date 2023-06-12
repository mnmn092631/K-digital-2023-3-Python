import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1, 13)  # 월별 데이터
sales = np.array([120, 145, 98, 156, 104, 176, 155, 140, 135, 120, 148, 170])  # 월별 판매량

plt.plot(months, sales, marker='o')

# 그래프 타이틀과 축 라벨 설정
plt.title('Monthly Sales Performance')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)


plt.show()