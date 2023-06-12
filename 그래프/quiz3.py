import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)  # 연도 데이터
gdp_a = np.array([100, 120, 150, 160, 180, 200, 220, 240, 260, 280, 300])  # A 나라의 연도별 GDP
gdp_b = np.array([80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])  # B 나라의 연도별 GDP
gdp_c = np.array([200, 220, 240, 250, 260, 270, 280, 290, 300, 310, 320])  # C 나라의 연도별 GDP

index = np.arange(len(years))

plt.bar(index - 0.25, gdp_a, 0.25, color = 'blue', label = 'Country A')
plt.bar(index, gdp_b, 0.25, color = 'red', label = 'Country B')
plt.bar(index + 0.25, gdp_c, 0.25, color = 'green', label = 'Country C')

plt.xticks(index, years)

plt.title("GDP Comparison by Country")
plt.xlabel("Years")
plt.ylabel("GDP (in billions)")

plt.grid(True)
plt.legend()

plt.show()