import pandas as pd
import matplotlib.pyplot as plt
import sys
import io

# 设置中文字体，避免图表中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 加载数据集并进行预处理
df = pd.read_csv("car_sales_data.csv")
df['Age'] = 2025 - df['Year of manufacture']
df = df.drop('Year of manufacture', axis=1)

# 第四问 使用散点图探索 Age（车龄）与 Price 之间的关系
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Price'], alpha=0.5, color='purple')
plt.title('车龄与价格关系散点图', fontsize=16)
plt.xlabel('车龄（年）', fontsize=14)
plt.ylabel('价格', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('age_price_scatter.png', dpi=300)
plt.show()

