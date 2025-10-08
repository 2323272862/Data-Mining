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

# 第三问使用直方图对 Price 的分布情况进行可视化展示
plt.figure(figsize=(12, 6))
counts, bins, patches = plt.hist(df['Price'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('汽车价格分布直方图', fontsize=16)
plt.xlabel('价格', fontsize=14)
plt.ylabel('频率', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for count, patch, bin_edge in zip(counts, patches, bins):
    if count > 0:  
        plt.text(bin_edge + (bins[1] - bins[0])/2, count, int(count),
                 ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig('price_distribution.png', dpi=300)
plt.show()

