import pandas as pd
import matplotlib.pyplot as plt
import sys
import io

# 设置中文字体，避免图表中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建answe2.txt文件，用于保存终端输出
output_file = open('answer2.txt', 'w', encoding='utf-8')
original_stdout = sys.stdout
output_buffer = io.StringIO()
sys.stdout = output_buffer

# 加载数据集并进行预处理
df = pd.read_csv("car_sales_data.csv")
df['Age'] = 2025 - df['Year of manufacture']
df = df.drop('Year of manufacture', axis=1)

# 第二问展示处理后数据集的总体信息（前五行）
print("处理后数据集的前五行：")
print(df.head())

# 计算所有数值型特征的描述性统计量
numeric_features = ['Engine size', 'Mileage', 'Price', 'Age']
descriptive_stats = df[numeric_features].describe()

# 将描述性统计量的英文表头替换为中文
chinese_labels = {
    'count': '计数',
    'mean': '均值',
    'std': '标准差', 
    'min': '最小值',
    '25%': '25%',
    '50%': '中位数',
    '75%': '75%',
    'max': '最大值'
}
descriptive_stats_zh = descriptive_stats.rename(index=chinese_labels)

print("\n所有数值型特征的描述性统计量：")
print(descriptive_stats_zh.round(2))

# 统计数据集中最常见的前5个汽车制造商及其数量
top5_manufacturers = df['Manufacturer'].value_counts().head(5)
print("\n最常见的前5个汽车制造商及其数量：")
print(top5_manufacturers)

# 可视化前5个常见汽车制造商的数量
plt.figure(figsize=(10, 6))
ax = top5_manufacturers.plot(kind='bar', color='skyblue')
plt.title('最常见的前5个汽车制造商及其数量', fontsize=14)
plt.xlabel('汽车制造商', fontsize=12)
plt.ylabel('车辆数量', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 5,
           f'{int(height)}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('top5_manufacturers.png', dpi=300)
plt.show()

# 将终端输出保存到answer2.txt文件中
sys.stdout = original_stdout
output_content = output_buffer.getvalue()
output_file.write(output_content)
output_file.close()

print(f"\n终端输出已保存到answer2.txt文件中")