import pandas as pd
import matplotlib.pyplot as plt
import sys
import io

# 设置中文字体，避免图表中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建answer.txt文件，用于保存终端输出
output_file = open('answer.txt', 'w', encoding='utf-8')
# 保存原始的stdout
original_stdout = sys.stdout
# 创建一个字符串IO对象来捕获输出
output_buffer = io.StringIO()
# 将stdout重定向到缓冲区
sys.stdout = output_buffer

# 加载数据集
df = pd.read_csv("car_sales_data.csv")

# 创建新特征Age（车龄）
df['Age'] = 2025 - df['Year of manufacture']

# 移除原有的Year of manufacture列
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
# 获取绘图对象的Axes实例
ax = top5_manufacturers.plot(kind='bar', color='skyblue')
plt.title('最常见的前5个汽车制造商及其数量', fontsize=14)
plt.xlabel('汽车制造商', fontsize=12)
plt.ylabel('车辆数量', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 在每个柱状上添加具体数值标签
for p in ax.patches:
    # 获取柱状的高度（即数值）
    height = p.get_height()
    # 在柱状上方添加文本标签，显示具体数值
    ax.text(p.get_x() + p.get_width() / 2., height + 5,
           f'{int(height)}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('top5_manufacturers.png', dpi=300)
plt.show()

# 恢复原始的stdout
sys.stdout = original_stdout
# 获取缓冲区中的内容
output_content = output_buffer.getvalue()
# 写入到文件
output_file.write(output_content)
# 关闭文件
output_file.close()

print(f"\n终端输出已保存到answer.txt文件中")