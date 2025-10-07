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

# 第三问使用直方图对 Price 的分布情况进行可视化展示
plt.figure(figsize=(12, 6))
counts, bins, patches = plt.hist(df['Price'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('汽车价格分布直方图', fontsize=16)
plt.xlabel('价格', fontsize=14)
plt.ylabel('频率', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 在每个柱状上标明具体的数量
for count, patch, bin_edge in zip(counts, patches, bins):
    if count > 0:  # 只在有数据的柱状上显示标签
        plt.text(bin_edge + (bins[1] - bins[0])/2, count, int(count),
                 ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig('price_distribution.png', dpi=300)
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