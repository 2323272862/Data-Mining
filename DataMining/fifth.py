import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import io

# 设置中文字体，避免图表中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 加载数据集并进行预处理
df = pd.read_csv("car_sales_data.csv")
df['Age'] = 2025 - df['Year of manufacture']
df = df.drop('Year of manufacture', axis=1)

# 第五问计算相关系数并且进行热力图呈现
numeric_features = ['Engine size', 'Mileage', 'Price', 'Age']
numeric_df = df[numeric_features]

# 计算spearman相关系数
corr_matrix = numeric_df.corr(method='spearman')

# 在终端输出相关系数
print("\n===== 数值型特征Spearman相关系数 =====")
print(corr_matrix.round(4))

# 将相关系数保存到spearman.txt文件中
with open('spearman.txt', 'w', encoding='utf-8') as f:
    f.write("===== 数值型特征Spearman相关系数 =====\n")
    f.write(f"{corr_matrix.round(4)}")

# 绘制热力图
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(corr_matrix, annot=True, cmap='YlOrRd', vmin=-1, vmax=1, 
                      linewidths=0.5, linecolor='white', fmt='.2f')
plt.title('数值型特征Spearman相关系数热力图', fontsize=16)
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300)
plt.show()

